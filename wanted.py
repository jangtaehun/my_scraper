from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)  # 기본값 True
# 우리가 브라우저를 볼 수 없다 -> headless mode

page = browser.new_page()

page.goto("https://www.wanted.co.kr")
time.sleep(3)

page.click("button.Aside_searchButton__Xhqq3")
# page.locator("button.Aside_searchButton__Xhqq3").click()
time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("python")
time.sleep(3)

page.keyboard.down("Enter")
time.sleep(3)

page.click("a#search_tab_position")
time.sleep(3)
for x in range(8):
    time.sleep(2)
    page.keyboard.down("End")

content = page.content()
p.stop()

soup = BeautifulSoup(content, "html.parser")
jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []
for job in jobs:
    link = f'https://www.wanted.co.kr{job.find("a")["href"]}'  # data-position-name 가능
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company = job.find("span", class_="JobCard_companyName__vZMqJ").text
    location = job.find("span", class_="JobCard_location__2EOr5").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    job = {
        "title": title,
        "company": company,
        "location": location,
        "reward": reward,
        "link": link,
    }
    jobs_db.append(job)
print(jobs_db)

# page.keyboard.down("End")
# time.sleep(3)
#
# page.keyboard.down("End")
# time.sleep(3)
#
# page.keyboard.down("End")
# time.sleep(3)

# page.screenshot(path='screenshot.png')

# file = open("jobs.csv", "w", encoding="utf-8")
# writter = csv.writer(file)
# writter.writerow(['Title', 'Company', 'Position', 'region', 'url']) #writerow는 list를 넣어줘야 한다.
# for job in all_jobs:
#     writter.writerow(job.values())
# file.close()
