from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)  # 기본값 True
# 우리가 브라우저를 볼 수 없다 -> headless mode

page = browser.new_page()

keyword = "python"

page.goto("https://www.jumpit.co.kr/")
time.sleep(3)

page.click("div.bOWajp > button")
time.sleep(3)

page.get_by_placeholder("검색어를 입력해주세요").fill(keyword)
# page.locator("button.Aside_searchButton__Xhqq3").click()
time.sleep(3)
