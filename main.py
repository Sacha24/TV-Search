import os
from bottle import get, post, redirect, request, route, run, static_file, template, error
import utils
import json


data = {
    "result": []
}


def load_data():
    AVAILABE_SHOWS = utils.AVAILABE_SHOWS
    for show in AVAILABE_SHOWS:
        showName = show
        show_info = utils.getJsonFromFile(showName)
        show_info = json.loads(show_info)
        data["result"].append(show_info)
        data["result"].sort(key=lambda x: x["name"])

# Static Routes


@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")


@route('/home')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/')
def handle_root_url():
    redirect("/home")


@route('/browse')
def browse():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=data["result"])


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


def main():
    load_data()
    run(host='localhost', port=os.environ.get('PORT', 7005))


if __name__ == "__main__":
    main()
