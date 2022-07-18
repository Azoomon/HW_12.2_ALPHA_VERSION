from flask import Flask, send_from_directory
from flask import Blueprint
from functions import search_posts_by_key
from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

"""регистрируем блюпринты"""
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)



@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

