import os
from bottle import get, post, redirect, request, route, run, static_file, template, error, response
import utils
import json

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
def load_shows():
    list_shows = [utils.getJsonFromFile(id) for id in utils.AVAILABE_SHOWS]
    list_shows.sort(key=lambda x: x["name"])
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=list_shows)


@route('/show/<show_id>')
def browse_show(show_id):
    show = utils.getJsonFromFile(int(show_id))
    if any(show):
        sectionTemplate = "./templates/show.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=show)
    else:
        response.status = 404
        sectionTemplate = "./templates/404.tpl"
        return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData=show)


@route('/ajax/show/<show_id>')
def browse_show(show_id):
    show = utils.getJsonFromFile(int(show_id))
    return template("./templates/show.tpl", result=show)


@route('/search')
def search():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


def main():
    run(host='localhost', port=os.environ.get('PORT', 7005))


if __name__ == "__main__":
    main()
