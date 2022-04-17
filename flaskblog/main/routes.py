from flask import render_template, request, Blueprint
from flask_login import LoginManager

main = Blueprint('main', __name__)
login_manger = LoginManager

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')
