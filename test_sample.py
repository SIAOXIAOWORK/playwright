from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        page.screenshot(path="example.png")
        browser.close()

def test_google_search(page):
    page.goto("https://www.google.com")
    page.fill("textarea[name=q]", "Playwright Python")
    page.click("input[name=btnK]")
    page.screenshot(path="google_search.png")


def test_google_title(page):
    page.goto("https://www.google.com")
    title = page.title()
    print(title)
    assert "Google" == title 

def test_bing_title(page):
    page.goto("https://www.bing.com")
    title = page.title()
    assert "bing" in title


def test_search_result(page):
    page.goto("https://www.bing.com/")
    page.fill("textarea[name=q]", "Playwright Python")
    page.click("label[id=search_icon]")
    page.screenshot(path="bing_search.png")
    page.wait_for_selector("h2")
    results = page.locator("h2")
    print (results)
    assert results.count() > 0