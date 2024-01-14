# Description: Main file for the LockDown project
import webbrowser
from flask import Flask, render_template, request
from modules.config import readAppConfig, updateAppConfig


app = Flask(__name__)
appcfg = readAppConfig()
language = appcfg["app_language"]
version = appcfg["app_version"]
author = appcfg["app_author"]

@app.route("/")
def index():
    if language == "":
        return render_template("language.html", version=version, language=language, author=author)
    return render_template("index.html", version=version, language=language, author=author)


@app.route("/status")
def status():
    return {"app": "LockDown", "status": "OK", "version": version, "language": language, "author": author}


if __name__ == "__main__":
    app.run(debug=True, port=4900)

