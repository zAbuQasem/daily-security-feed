"""
Playwright E2E tests for the deployed site.
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
    expect(page).to_have_title(re.compile(r"Security Feed Monitor"))


def test_sidebar_title(page: Page):
    page.goto(BASE)
    title = page.locator("#sidebar .brand__title")
    expect(title).to_contain_text("Security Feed Monitor")


def test_sidebar_home_link(page: Page):
    page.goto(BASE)
    home = page.locator("#sidebar .sidebar-nav a")
    expect(home.first).to_contain_text("Home")


def test_sidebar_theme_toggle(page: Page):
    page.goto(BASE)
    toggle = page.locator("#themeToggle")
    expect(toggle).to_be_visible()


def test_posts_visible_on_homepage(page: Page):
    page.goto(BASE)
    posts = page.locator(".article-row")
    assert posts.count() > 0, "No posts visible on homepage"


def test_date_groups_on_homepage(page: Page):
    page.goto(BASE)
    groups = page.locator(".date-card")
    assert groups.count() > 0, "No date groups on homepage"


def test_tag_filters_visible(page: Page):
    page.goto(BASE)
    filters = page.locator("#tagFilters .tag")
    assert filters.count() > 5, "Expected tag filter pills"


def test_search_bar_visible(page: Page):
    page.goto(BASE)
    expect(page.locator("#searchInput")).to_be_visible()


def test_no_severity_categories(page: Page):
    """Severity labels (Critical, Solid, Low) should not appear in post metadata."""
    page.goto(BASE)
    for severity in ["Critical", "Solid", "Low"]:
        badges = page.locator(f'a.badge:has-text("{severity}"), .categories a:has-text("{severity}")')
        assert badges.count() == 0, f"Severity '{severity}' found in category badges"


# ── Individual post ──


def test_post_page_has_content(page: Page):
    page.goto(BASE)
    page.wait_for_load_state("networkidle")
    first_post = page.locator(".article-row__title").first
    first_post.click()
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator("h1.post-article__title")).to_be_visible()
    expect(page.locator(".post-article__body")).to_be_visible()


def test_post_has_read_original_link(page: Page):
    page.goto(BASE)
    page.wait_for_load_state("networkidle")
    first_post = page.locator(".article-row__title").first
    first_post.click()
    page.wait_for_load_state("domcontentloaded")
    expect(page.locator("text=Read original article")).to_be_visible()


def test_post_back_link(page: Page):
    page.goto(BASE)
    page.wait_for_load_state("networkidle")
    page.locator(".article-row__title").first.click()
    page.wait_for_load_state("domcontentloaded")
    back = page.locator(".post-article__back")
    expect(back).to_be_visible()
    expect(back).to_contain_text("Back to feed")


def test_post_shows_tags(page: Page):
    page.goto(BASE)
    page.wait_for_load_state("networkidle")
    page.locator(".article-row__title").first.click()
    page.wait_for_load_state("domcontentloaded")
    tags = page.locator(".post-article__tags .tag")
    assert tags.count() > 0, "No tags shown on post page"


# ── Dark mode ──


def test_dark_mode_toggle(page: Page):
    page.goto(BASE)
    toggle = page.locator("#themeToggle")
    initial = page.evaluate("document.documentElement.getAttribute('data-theme')")
    toggle.click()
    after = page.evaluate("document.documentElement.getAttribute('data-theme')")
    assert initial != after, "Theme did not change after toggle"
