# Description: Main file for the LockDown project
import webbrowser
from flask import Flask, render_template, request
from modules.config import readAppConfig, updateAppConfig


app = Flask(__name__)
appcfg = readAppConfig()
language = appcfg["app_language"]
version = appcfg["app_version"]


@app.route("/")
def index():
    return render_template("html/index.html")


@app.route("/status")
def status():



if __name__ == "__main__":
    webbrowser.open("http://localhost:4900")
    # On port already in use error che
    app.run(port=4900, debug=True)