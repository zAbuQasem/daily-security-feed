"""
injection_scanner.py

Prompt-injection pre-filter — blocks malicious content before it reaches
the Copilot CLI so the AI never sees adversarial instructions.

Attackers embed adversarial instructions in RSS content using obfuscation:
  - Unicode homoglyphs (Cyrillic і vs Latin i)
  - Zero-width / invisible characters
  - Fullwidth Latin (ｉｇｎｏｒｅ)
  - Base64-encoded payloads
  - HTML entities (&#105;gnore)
  - URL-percent encoding (%69gnore)
  - Leetspeak substitutions (1gn0re)
  - Multi-language injection (Arabic, Chinese, Russian, etc.)

The scanner normalises text through all these layers before matching.
"""

import base64
import html
import re
import unicodedata
from urllib.parse import unquote as url_unquote

# -- Homoglyph map: visually similar characters → ASCII equivalent ----------
_HOMOGLYPHS: dict[str, str] = {
    # Cyrillic
    "\u0430": "a",
    "\u0410": "A",  # а А
    "\u0435": "e",
    "\u0415": "E",  # е Е
    "\u043e": "o",
    "\u041e": "O",  # о О
    "\u0440": "p",
    "\u0420": "P",  # р Р
    "\u0441": "c",
    "\u0421": "C",  # с С
    "\u0443": "y",
    "\u0423": "Y",  # у У
    "\u0456": "i",
    "\u0406": "I",  # і І  (Ukrainian)
    "\u0458": "j",  # ј
    "\u04bb": "h",  # һ
    "\u0445": "x",
    "\u0425": "X",  # х Х
    # Greek
    "\u03b1": "a",
    "\u0391": "A",  # α Α
    "\u03b5": "e",
    "\u0395": "E",  # ε Ε
    "\u03bf": "o",
    "\u039f": "O",  # ο Ο
    "\u03c1": "p",  # ρ
    "\u03ba": "k",  # κ
    "\u03bd": "v",  # ν
    # Latin-like symbols
    "\u2026": "...",  # …
    "\uff01": "!",  # ！
    "\u2018": "'",
    "\u2019": "'",  # '' smart quotes
    "\u201c": '"',
    "\u201d": '"',  # "" smart quotes
}

# -- Leetspeak map ---------------------------------------------------------
_LEET: dict[str, str] = {
    "0": "o",
    "1": "i",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t",
    "@": "a",
    "$": "s",
    "!": "i",
    "|": "i",
}


def _url_decode_fully(text: str) -> str:
    """Decode URL percent-encoding iteratively to defeat double/triple encoding."""
    for _ in range(5):
        decoded = url_unquote(text)
        if decoded == text:
            break
        text = decoded
    return text


def _normalise_text(text: str) -> str:
    """Reduce obfuscated text to plain ASCII for pattern matching.

    Pipeline: HTML entity decode -> URL percent-decode (iterative) -> Unicode
    NFKD (collapses fullwidth) -> strip zero-width/invisible chars -> homoglyph
    substitution -> leetspeak substitution -> lowercase -> collapse whitespace.
    """
    # 1. HTML entity decode (handles &#105; &#x69; &amp; etc.)
    text = html.unescape(text)

    # 2. URL percent-decode iteratively (handles %2569 double-encoding etc.)
    text = _url_decode_fully(text)

    # 3. Unicode NFKD normalisation — maps fullwidth ｉ→i, ligatures ﬁ→fi, etc.
    text = unicodedata.normalize("NFKD", text)

    # 4. Replace zero-width and invisible characters with a space so that
    #    words separated only by them don't merge into a single token
    text = re.sub(
        r"[\u200b\u200c\u200d\u200e\u200f\ufeff\u00ad\u034f"
        r"\u061c\u2060\u2061\u2062\u2063\u2064\u206a-\u206f]+",
        " ",
        text,
    )

    # 5. Homoglyph substitution
    text = "".join(_HOMOGLYPHS.get(ch, ch) for ch in text)

    # 6. Leetspeak substitution
    text = "".join(_LEET.get(ch, ch) for ch in text)

    # 7. Lowercase
    text = text.lower()

    # 8. Collapse whitespace (tabs, multiple spaces, non-breaking spaces)
    text = re.sub(r"\s+", " ", text)

    return text


# -- Multi-language injection patterns ------------------------------------
_MULTILANG_PATTERNS: list[re.Pattern[str]] = [
    re.compile(p, re.IGNORECASE)
    for p in [
        # Arabic
        r"تجاهل\s+(جميع\s+)?التعليمات",  # "ignore (all) instructions"
        r"تجاهل\s+الأوامر\s+السابقة",  # "ignore previous commands"
        # Chinese (Simplified)
        r"忽略.{0,4}(之前的|以上的|所有的)?指[令示]",  # "ignore (previous/all) instructions"
        r"无视.{0,4}(之前的|以上的)?规则",  # "disregard (previous) rules"
        # Chinese (Traditional)
        r"忽略.{0,4}(之前的|以上的|所有的)?指[令示]",
        # Russian
        r"игнорируй(те)?\s+(все\s+)?(предыдущие\s+)?инструкции",
        r"забудь(те)?\s+(все\s+)?правила",
        # Spanish
        r"ignora\s+(todas?\s+)?(las\s+)?(instrucciones|reglas)\s+(anteriores|previas)",
        # French
        r"ignore[rz]?\s+(toutes?\s+)?(les\s+)?(instructions|règles)\s+(précédentes|ci-dessus)",
        # German
        r"ignoriere?\s+(alle\s+)?(vorherigen?\s+)?(anweisungen|regeln)",
        # Portuguese
        r"ignore\s+(todas?\s+)?(as\s+)?(instruções|regras)\s+(anteriores|acima)",
        # Japanese
        r"(以前の|上記の)?指示を無視",  # "ignore (previous) instructions"
        # Korean
        r"(이전|위의)?\s*지시를?\s*무시",  # "ignore (previous) instructions"
        # Turkish
        r"(önceki\s+)?(talimatları|kuralları)\s+(yok\s+say|görmezden\s+gel)",
        # Hindi
        r"(पिछले\s+)?निर्देशों\s+को\s+अनदेखा\s+कर",
    ]
]

# -- Core English injection patterns (applied after normalisation) ---------
_INJECTION_PATTERNS: list[re.Pattern[str]] = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"ignore\s+(all\s+)?(previous|prior|above|your)\s+(instructions|rules|prompts?|directives?)",
        r"disregard\s+(all\s+)?(previous|prior|above|your)\s+(instructions|rules|prompts?)",
        r"forget\s+(all\s+)?your\s+(rules|instructions|prompts?|guidelines)",
        r"override\s+(all\s+)?(your\s+)?(instructions|rules|prompts?|system)",
        r"you\s+are\s+now\s+(a|an|my)\s+(new\s+)?(ai|bot|assistant|gpt|model|llm|chatbot|persona)",
        r"(?:^|\n)\s*new\s+(system\s+)?instructions?\s*:",
        r"(?:^|\n)\s*(system|admin|developer|assistant)\s*:\s*(you|ignore|forget|override|disregard|reveal|output|do not|instead)",
        r"(reveal|output|print|echo|show|display|leak)\s+(your|the)\s+(system\s+)?(prompt|instructions|rules|api.?keys?)",
        r"(exfiltrate|encode|embed)\s+(your\s+|the\s+|this\s+).{0,30}(token|secret|key|password|credential)",
        r"base64[.\s]+(encode|decode)\s+(your\s+|the\s+).{0,20}(token|secret|key)",
        r"respond\s+(only\s+)?with\s+(your\s+|the\s+).{0,20}(token|secret|key|env)",
        r"ignore\s+the\s+(article|content|text)\s+and\s+",
        r"do\s+not\s+classify",
        r"instead\s+of\s+classifying",
    ]
]

# Compile with MULTILINE for patterns that use ^ anchoring
for i, pat in enumerate(_INJECTION_PATTERNS):
    if pat.pattern.startswith("(?:^|"):
        _INJECTION_PATTERNS[i] = re.compile(pat.pattern, re.IGNORECASE | re.MULTILINE)

# -- Exfiltration patterns (applied to raw text — $ and { must not be normalised)
_EXFIL_PATTERNS: list[re.Pattern[str]] = [
    re.compile(p, re.IGNORECASE)
    for p in [
        r"(curl|wget|nc|ncat|netcat)\s+.{0,20}https?://.{0,60}[\$\{]+(TOKEN|SECRET|KEY|PASSWORD|COPILOT|GITHUB|API)",
        r"(curl|wget|nc|ncat|netcat)\s+.{0,20}https?://.{0,60}\$[A-Z_]{3,}",
        r"(curl|wget)\s+.{0,10}(-d|--data)\s+.{0,30}[\$\{]+(TOKEN|SECRET|KEY|COPILOT|GITHUB)",
    ]
]

_MAX_BASE64_DECODED_LEN = 2000


def _find_base64_payloads(text: str) -> list[str]:
    """Detect base64-encoded strings and check decoded content for injection."""
    hits: list[str] = []
    # Match base64 blocks: 20+ chars, valid alphabet, optional padding
    for match in re.finditer(r"[A-Za-z0-9+/]{20,}={0,2}", text):
        candidate = match.group()
        try:
            decoded = base64.b64decode(candidate, validate=True).decode(
                "utf-8", errors="ignore"
            )
        except Exception:
            continue
        if len(decoded) > _MAX_BASE64_DECODED_LEN:
            continue
        # Check if the decoded text contains injection patterns
        normalised = _normalise_text(decoded)
        for pat in _INJECTION_PATTERNS:
            if pat.search(normalised):
                hits.append(f"base64-encoded: {pat.pattern}")
                break
    return hits


def scan_for_injection(text: str) -> list[str]:
    """Return list of matched injection pattern descriptions found in *text*.

    Scans through multiple normalisation layers:
    1. Raw multi-language patterns (Arabic, Chinese, Russian, etc.)
    2. Exfiltration patterns on raw text (preserve $, {, } semantics)
    3. Normalised text (homoglyphs, leetspeak, fullwidth, HTML entities, etc.)
    4. Base64-encoded payloads
    """
    if not text or not isinstance(text, str):
        return []

    hits: list[str] = []

    # 1. Multi-language patterns on raw text (these are already Unicode-native)
    for pat in _MULTILANG_PATTERNS:
        if pat.search(text):
            hits.append(f"multilang: {pat.pattern}")

    # 2. Exfiltration patterns on raw text ($ and { have meaning here)
    for pat in _EXFIL_PATTERNS:
        if pat.search(text):
            hits.append(f"exfil: {pat.pattern}")

    # 3. Normalise and match English patterns
    normalised = _normalise_text(text)
    for pat in _INJECTION_PATTERNS:
        if pat.search(normalised):
            hits.append(pat.pattern)

    # 4. Check for base64-encoded injection payloads
    hits.extend(_find_base64_payloads(text))

    return hits
