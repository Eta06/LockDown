# Description: Main file for the LockDown project
import webbrowser
from flask import Flask, render_template, request, redirect, url_for
from modules.config import readAppConfig, updateAppConfig, loadLanguageFiles


app = Flask(__name__)
appcfg = readAppConfig()
language = appcfg["app_language"]
language_files = loadLanguageFiles(language)
print(language_files)
version = appcfg["app_version"]
author = appcfg["app_author"]


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


@app.route("/")
def index():
    if language == "":
        return render_template("language.html", version=version, language=language, author=author)
    return render_template("index.html", version=version, language=language, author=author)


@app.route("/status")
def status():
    return {"app": "LockDown", "status": "OK", "version": version, "language": language, "author": author}


if __name__ == "__main__":
    webbrowser.open("http://192.168.1.230:4900/")
    app.run(debug=True, port=4900, host="0.0.0.0")

