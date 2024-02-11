from file import save_wanted, save_jumpit
from wanted import scrap_wanted
from jumpit import scrap_jumpit
from flask import Flask, render_template, request, redirect, send_file

app = Flask("new scraper")

wanted_db = {}
jumpit_db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/search_wanted")
def first_search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in wanted_db:
        jobs = wanted_db[keyword]
    else:
        jobs = scrap_wanted(keyword)
        wanted_db[keyword] = jobs
        print(wanted_db)
    return render_template("search_wanted.html", keyword=keyword, jobs=jobs)


@app.route("/search_jumpit")
def second_search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in jumpit_db:
        jobs = jumpit_db[keyword]
    else:
        jobs = scrap_jumpit(keyword)
        jumpit_db[keyword] = jobs
    return render_template("search_jumpit.html", keyword=keyword, jobs=jobs)


@app.route("/export_wanted")
def export_wanted():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in wanted_db:
        return redirect(f"/search_wanted?keyword={keyword}")

    save_wanted(keyword, wanted_db[keyword])
    print(f"wanted_{keyword}.csv")
    return send_file(
        f"wanted_{keyword}.csv",
        as_attachment=True,
        mimetype="text/csv; charset=UTF-8",
    )


@app.route("/export_jumpit")
def export_jumpit():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in jumpit_db:
        return redirect(f"/search_jumpit?keyword={keyword}")

    save_jumpit(keyword, jumpit_db[keyword])
    print(f"jumpit_{keyword}.csv")
    return send_file(f"jumpit_{keyword}.csv", as_attachment=True)


app.run("127.0.0.1", port=5000)
