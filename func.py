from flask import Flask, render_template

app = Flask(__name__)


def error(message, code=400):
    return render_template("error.html", code=code, message=message)