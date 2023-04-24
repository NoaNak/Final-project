from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     title = "John Elder's Blog"
#     return render_template("index.html", title=title)

# @app.route('/about')
# def about():
#     title = "About John Elder"
#     return render_template("about.html", names=names, title=title)

