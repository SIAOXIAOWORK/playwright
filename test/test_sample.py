import pytest
from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")
        page.screenshot(path="example.png")
        browser.close()

def test_google_search(browser_page):
    browser_page.goto("https://www.google.com")
    browser_page.fill("textarea[name=q]", "Playwright Python")
    browser_page.click("input[name=btnK]")
    browser_page.screenshot(path="google_search.png")

def test_google_title(browser_page):
    browser_page.goto("https://www.google.com")
    title = browser_page.title()
    print(title)
    assert "Google" == title 

def test_bing_title(browser_page):
    browser_page.goto("https://www.bing.com")
    title = browser_page.title()
    assert "Bing" in title

@pytest.mark.parametrize("url, keyword",[("https://www.google.com","Google"),("https://www.bing.com","Bing")])
def test_search_engines_title(browser_page, url, keyword):
    browser_page.goto(url)
    title = browser_page.title()
    assert keyword in title


def test_search_result(browser_page):
    browser_page.goto("https://www.bing.com/")
    browser_page.screenshot(path="bing_search.png")
    browser_page.fill("textarea[name=q]", "Playwright Python")
    browser_page.click("label[id=search_icon]")
    browser_page.screenshot(path="bing_search.png")
    browser_page.wait_for_selector("h2")
    results = browser_page.locator("h2")
    print (results)
    assert results.count() > 0



def test_add_todo(browser_page):
    browser_page.goto("https://demo.playwright.dev/todomvc")
    browser_page.fill(".new-todo", "Buy milk")
    browser_page.press(".new-todo", "Enter")
    items = browser_page.locator(".todo-list li")
    assert items.count() == 1
    assert items.nth(0).text_content() == "Buy milk"
    items.nth(0).hover() # 等於讓游標指在該項目上，因為有些元素需要保持在該元素上才會顯示其他元素
    assert items.nth(0).locator("button[class=destroy]").is_visible()
    items.nth(0).locator("button[class=destroy]").click()
    assert items.count() == 0