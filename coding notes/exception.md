今天驗證有錯誤時，可以使用例外處裡的方式進行截圖
```python
def test_faild_case(browser_page):

    browser_page.goto("https://www.bing.com/")

    title = browser_page.title()

    try:

        assert "123456" in title

    except AssertionError:

        browser_page.screenshot(path="test_faild_case(fail).png")

        raise
```

<span style = 'color :red'>注意</span>  如果要使用例外處裡 需要記得<span style = 'color: red'>raise</span> 不然會直接被pytest認為該case狀態為通過

