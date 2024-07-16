# Description: Main file for the LockDown project
import webbrowser
from flask import Flask, render_template, request, redirect, url_for
from modules.config import readAppConfig, updateAppConfig, loadLanguageFiles, tryLoad


app = Flask(__name__)
appcfg = readAppConfig()
language = tryLoad("app_language")
language_files = loadLanguageFiles(language)
version = tryLoad("app_version")
author = tryLoad("app_author")
port = tryLoad("app_port")


@app.route("/set_language", methods=["POST"])
def set_language():
    import time
    time.sleep(1)
    global language
    global language_files

    selection = request.form.get("language")

    appcfg["app_language"] = selection
    updateAppConfig("app_language", selection)

    language_files = loadLanguageFiles(selection)
    language = selection

    return redirect(url_for("index"))


@app.route("/reset_everything", methods=["POST"])
def reset_everything():
    global language
    global language_files

    appcfg["app_language"] = ""
    updateAppConfig("app_language", "")
    updateAppConfig("app_port", "4900")
    language_files = loadLanguageFiles("")
    language = ""

    return redirect(url_for("index"))


@app.route("/")
def index():
    if language == "":
        return render_template("language.html", version=version, language=language, author=author)
    return render_template("index.html", version=version, language=language, author=author, language_files=language_files)


@app.route("/status")
def status():
    return {"app": "LockDown", "status": "OK", "version": version, "language": language, "author": author}


if __name__ == "__main__":
    appcfg = readAppConfig()
    app_port = tryLoad("app_port")
    webbrowser.open("http://localhost:" + str(app_port))
    app.run(debug=True, port=app_port, host="0.0.0.0")

