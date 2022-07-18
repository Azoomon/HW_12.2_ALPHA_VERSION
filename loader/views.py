from flask import Blueprint, render_template, request
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post/", methods=["GET", "POST"])
def page_post_form():
    if request.method == "POST":
        return render_template("post_uploaded.html")
    return render_template("post_form.html")

