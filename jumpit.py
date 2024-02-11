from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
from file import save_jumpit


def scrap_jumpit(keyword):
    p = sync_playwright().start()
    browser = p.chromium.launch(headless=True)  # 기본값 True: 웹 안 뜸
    page = browser.new_page()

    jobs_db = []

    page.goto("https://www.jumpit.co.kr/")
    page.click("div.bOWajp > button")
    page.get_by_placeholder("검색어를 입력해주세요").fill(keyword)

    page.click("button.search_button")
    time.sleep(1)
    for x in range(8):
        time.sleep(2)
        page.keyboard.down("End")

    content = page.content()
    p.stop()

    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="sc-c8169e0e-0")

    for job in jobs:
        link = f'https://www.jumpit.co.kr/{job.find("a")["href"]}'  # data-position-name 가능
        title = job.find("h2", class_="position_card_info_title").text
        company = job.find("div", class_="sc-635ec9d6-0").find("div").text
        location = job.find("ul", class_="egeNa-D").find_all("li")[0].text
        career = job.find("ul", class_="egeNa-D").find_all("li")[1].text
        job = {
            "title": title,
            "company": company,
            "location": location,
            "link": link,
            "career": career,
            "reward": "",
        }
        jobs_db.append(job)
    # save_jumpit(keyword, jobs_db)
    return jobs_db


# scrap_jumpit("python")
# print(scrap_jumpit("python"))
