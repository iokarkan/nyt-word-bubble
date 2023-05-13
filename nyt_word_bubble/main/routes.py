import os
from flask import (
    render_template,
)
from . import bp as main
from werkzeug.http import HTTP_STATUS_CODES

basedir = os.path.abspath(os.path.dirname(__file__))

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/info")
def info():
    return "<h1>TO-DO</h1>"