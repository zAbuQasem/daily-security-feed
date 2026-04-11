"""
Playwright E2E tests for the deployed Chirpy site.
Run with: uv run pytest tests/test_site.py -v
"""

import re

import pytest
from playwright.sync_api import Page, expect

BASE = "https://zabuqasem.github.io/security-feed-monitor"


@pytest.fixture(scope="session")
def browser_context_args():
    return {"ignore_https_errors": True}


# ── Homepage ──


def test_homepage_loads(page: Page):
    page.goto(BASE)
    expect(page).to_have_title(re.compile(r"Daily Security Feed"))


def test_avatar_visible(page: Page):
    page.goto(BASE)
    avatar = page.locator('img[alt="avatar"]')
    expect(avatar).to_be_visible()
    assert "rss-icon" in (avatar.get_attribute("src") or "")


def test_sidebar_title(page: Page):
    page.goto(BASE)
    title = page.locator("#sidebar .site-title, #sidebar a.site-title")
    expect(title).to_contain_text("Daily Security Feed")


def test_sidebar_nav_links(page: Page):
    page.goto(BASE)
    nav = page.locator("#sidebar .nav-item")
    labels = [nav.nth(i).inner_text().strip().upper() for i in range(nav.count())]
    for expected in ["HOME", "CATEGORIES", "TAGS", "ARCHIVES", "ABOUT"]:
        assert expected in labels, f"Missing nav link: {expected}"


def test_posts_visible_on_homepage(page: Page):
    page.goto(BASE)
    # Chirpy lists posts as article or .post-preview or card-body elements
    posts = page.locator("article, .card-body, .post-preview")
    assert posts.count() > 0, "No posts visible on homepage"


def test_no_severity_categories(page: Page):
    """Severity labels (Critical, Solid, Low) should not appear in post metadata."""
    page.goto(BASE)
    for severity in ["Critical", "Solid", "Low"]:
        badges = page.locator(f'a.badge:has-text("{severity}"), .categories a:has-text("{severity}")')
        assert badges.count() == 0, f"Severity '{severity}' found in category badges"


# ── Tags page ──


def test_tags_page_loads(page: Page):
    page.goto(f"{BASE}/tags/")
    expect(page).to_have_title(re.compile(r"Tags"))


def test_tags_page_has_tags(page: Page):
    page.goto(f"{BASE}/tags/")
    tags = page.locator("#tags-container .tag-name, #tags a, .tag")
    assert tags.count() > 5, f"Expected many tags, got {tags.count()}"


def test_individual_tag_page_loads(page: Page):
    """Clicking a tag should load a page listing posts for that tag."""
    page.goto(f"{BASE}/tags/cloud/")
    expect(page).to_have_title(re.compile(r"cloud", re.IGNORECASE))
    posts = page.locator("article a, .post-preview a, ul li a")
    assert posts.count() > 0, "No posts listed on tag page"


# ── Categories page ──


def test_categories_page_loads(page: Page):
    page.goto(f"{BASE}/categories/")
    expect(page).to_have_title(re.compile(r"Categories"))


def test_category_is_rss(page: Page):
    """All posts should be under the RSS category."""
    page.goto(f"{BASE}/categories/")
    expect(page.locator("text=RSS")).to_be_visible()


# ── Archives page ──


def test_archives_page_loads(page: Page):
    page.goto(f"{BASE}/archives/")
    expect(page).to_have_title(re.compile(r"Archives"))


# ── About page ──


def test_about_page_loads(page: Page):
    page.goto(f"{BASE}/about/")
    expect(page).to_have_title(re.compile(r"About"))
    expect(page.locator("main")).to_contain_text("AI-curated")


# ── Individual post ──


def test_post_page_has_content(page: Page):
    page.goto(BASE)
    # Click the first post link
    first_post = page.locator("article a, .card-body a, .post-preview a").first
    first_post.click()
    page.wait_for_load_state("domcontentloaded")
    # Post page should have a title and body content
    expect(page.locator("h1")).to_be_visible()
    body = page.locator(".post-content, article .content, .post")
    assert body.count() > 0, "No post content found"


def test_post_has_read_original_link(page: Page):
    page.goto(BASE)
    first_post = page.locator("article a, .card-body a, .post-preview a").first
    first_post.click()
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator("text=Read original article")).to_be_visible()
