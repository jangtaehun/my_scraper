import csv


def save_wanted(keyword, jobs_db):
    file = open(f"wanted_{keyword}.csv", "w", encoding="CP949")
    writter = csv.writer(file)
    writter.writerow(
        ["Title", "Company", "Position", "region", "url"]
    )  # writerow는 list를 넣어줘야 한다.
    for job in jobs_db:
        writter.writerow(job.values())
    file.close()


def save_jumpit(keyword, jobs_db):
    file = open(f"jumpit_{keyword}.csv", "w", encoding="CP949")
    writter = csv.writer(file)
    writter.writerow(["Title", "Company", "Position", "region", "url"])
    for job in jobs_db:
        writter.writerow(job.values())
    file.close()
