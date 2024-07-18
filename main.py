# Description: Main file for the LockDown project
import os
from flask import Flask, render_template, request, redirect, url_for
from modules.config import readAppConfig, updateAppConfig, loadLanguageFiles, tryLoad
import sys

app = Flask(__name__)
appcfg = readAppConfig()
language = tryLoad("app_language")
language_files = loadLanguageFiles(language)
version = tryLoad("app_version")
author = tryLoad("app_author")
port = tryLoad("app_port")


def restart_server():
    """Restarts the current Python script."""
    print("Restarting server...")
    python = sys.executable
    # Close stdout and stderr to prevent inheritance
    with open(os.devnull, 'wb') as devnull:
        os.dup2(devnull.fileno(), sys.stdout.fileno())
        os.dup2(devnull.fileno(), sys.stderr.fileno())
        os.execl(python, python, *sys.argv)


@app.route("/language_data")
def get_language_data():
    return {
        "lang": language_files,
        "config": appcfg
    }


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


@app.route("/set_port", methods=["POST"])
def set_port():
    global port

    port = request.form.get("port")
    if port == "" or not port.isdigit() or int(port) < 1024 or int(port) > 65535:
        return redirect(url_for("index"))
    appcfg["app_port"] = port
    updateAppConfig("app_port", port)

    restart_server()  # Restart instead of shutdown
    return 'Server restarting...'  # Indicate restart in progress


@app.route("/")
def index():
    if language == "":
        return render_template("language.html", version=version, language=language, author=author)
    return render_template("index.html", version=version, language=language, author=author,
                           language_files=language_files, port=port)


if __name__ == "__main__":
    while True:
        appcfg = readAppConfig()
        app_port = tryLoad("app_port")
        # webbrowser.open("http://localhost:" + str(app_port))
        app.run(debug=True, port=app_port, host="0.0.0.0")