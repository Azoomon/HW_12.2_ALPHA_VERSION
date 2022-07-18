from flask import Blueprint, render_template, request   #заводим все необходимые модули
from functions import search_posts_by_key

#задаем блюпринт (в аргументе даем название, присваиваем к app.py (__name__) и подвязываем к шаблонам html)
main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

"""объявляем вьюшки с помощью блюпринтов, возвращая соответсвующие html-шаблоны"""
@main_blueprint.route("/")
def page_index():
    return  render_template("index.html")

"""функция поиска по ключевым словам"""
@main_blueprint.route("/search/")
def page_tag():
    search_txt = request.values.get("s")
    posts = search_posts_by_key(search_txt)
    return render_template("post_list.html", posts=posts, search_txt=search_txt)

