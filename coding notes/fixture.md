參數
- scope: 預設為function，另外 module、class、session
- name: 設定fixture別名，預設為function名稱
- autouse: 預設為False，啟用了話會自動進行使用（根據scope設定而定）



規則
- 當想要使用兩個以上的fixture時會有兩個狀況
	- 有依賴：會依照依賴的先後順序執行
	- 沒依賴：會依照參數的輸入順序執行




預設fixture: page
	會再測項結束後關閉page/context
	browser則是在整個測試結束後才關閉，所以如果中間有混著用自己建立的sync_playwright()，就會發生error:`It looks like you are using Playwright Sync API inside the asyncio loop.`