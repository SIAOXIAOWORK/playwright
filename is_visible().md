用來判斷元素是否顯示在畫面上
如果DOM中找不到該元素，會報錯


page.is_visible(selector, \*\*kwargs) -> bool

element exist in DOM and visible in screen -> true
element exist in DOM but invisible in screen -> false
element doesn't exist in DOM -> exception