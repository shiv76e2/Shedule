from flask import render_template, request, Blueprint
from flask_login import LoginManager
from flaskblog.models import Room

main = Blueprint('main', __name__)
login_manger = LoginManager

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/about")
def about():
    return render_template('about.html')


@main.route('/rooms')
def rooms():
    rooms = Room.query.all()
    return render_template('rooms.html', title='部屋', rooms=rooms)

@main.route('/reserve')
def reserve():
    return render_template('reserve.html')

@main.route('/schedule')
def schedule():
    return render_template('schedule.html')