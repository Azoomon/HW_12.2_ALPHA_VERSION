from flask import Flask, send_from_directory
from loader.views import loader_blueprint
from main.views import main_blueprint


UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

"""регистрируем блюпринты"""
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


"""Вьюшка для добавленного поста"""
@app.route("/uploads/<path:path>/")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()

