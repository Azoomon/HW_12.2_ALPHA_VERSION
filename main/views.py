from flask import Blueprint, render_template, request
from functions import search_posts_by_key

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def page_index():
    return  render_template("index.html")


@main_blueprint.route("/search/")
def page_tag():
    search_txt = request.values.get("s")
    posts = search_posts_by_key(search_txt)
    return render_template("post_list.html", posts=posts, search_txt=search_txt)

