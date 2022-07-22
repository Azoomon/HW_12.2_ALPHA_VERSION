from flask import Blueprint, render_template, request
from functions import dump_json, is_filename_allowed
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post/", methods=["GET", "POST"])
def page_post_form():
    if request.method == "POST":
        picture = request.files.get('picture')
        content = request.form.get('content')
        filename = picture.filename
        if not content:
            return "Нет текста"
        if not picture:
            return "Вы не добавили фото"
        if is_filename_allowed(filename) is None:
            return "Тип файла некорректный"

        picture.save(f"./uploads/images/{filename}")
        post = dump_json(filename, content)
        return render_template("post_uploaded.html", post=post)
    return render_template("post_form.html")

