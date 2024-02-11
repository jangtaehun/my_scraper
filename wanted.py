from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from file import save_wanted


def scrap_wanted(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=False)  # 기본값 True: 웹 안 뜸
    # 우리가 브라우저를 볼 수 없다 -> headless mode
    page = browser.new_page()
    jobs_db = []

    page.goto("https://www.wanted.co.kr")
    page.click("button.Aside_searchButton__Xhqq3")
    # page.locator("button.Aside_searchButton__Xhqq3").click()
    page.get_by_placeholder("검색어를 입력해 주세요.").fill(keyword)
    page.keyboard.down("Enter")

    page.click("a#search_tab_position")
    time.sleep(1)
    for x in range(8):
        time.sleep(1)
        page.keyboard.down("End")

    content = page.content()
    p.stop()

    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")

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
            "link": link,
            "career": "",
            "reward": reward,
        }
        jobs_db.append(job)
    # save_wanted(keyword, jobs_db)
    return jobs_db


# print(scrap_wanted("python"))

# scrap_wanted()
# print(jobs_db)

# page.keyboard.down("End")
# time.sleep(3)
#
# page.keyboard.down("End")
# time.sleep(3)
#
# page.keyboard.down("End")
# time.sleep(3)

# page.screenshot(path='screenshot.png')


# def save_wanted(keyword, jobs_db):
#     file = open(f"wanted_{keyword}.csv", "w", encoding="utf-8")
#     writter = csv.writer(file)
#     writter.writerow(
#         ["Title", "Company", "Position", "region", "url"]
#     )  # writerow는 list를 넣어줘야 한다.
#     for job in jobs_db:
#         writter.writerow(job.values())
#     file.close()
