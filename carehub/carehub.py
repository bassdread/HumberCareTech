from flask import Flask, render_template

# EB looks for an 'application' callable by default.
application = Flask(__name__)


def say_hello(username="World"):
    return render_template('index.html', name=username)


def login():
    return render_template('login.html')


def careplan():
    return render_template('careplan.html')


application.add_url_rule('/login', view_func=login)
application.add_url_rule('/test', view_func=careplan)

