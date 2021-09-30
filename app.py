from datetime import timedelta
from flask import Flask, flash, redirect, render_template, request, session
import sqlite3

from func import error

app = Flask(__name__)

con = sqlite3.connect("test.db", check_same_thread=False)
db = con.cursor()
con.commit()

app.debug = True
app.config.update(DEBUG=True)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = 'SECRETKEY'

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/', methods=["POST", "GET"])
def index():
    
    return render_template("index.html")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return error(e.name, e.code)