from flask import render_template, request, Blueprint
from flask_login import LoginManager
from flaskblog.models import Room

rooms = Blueprint('rooms', __name__)


@rooms.route('/rooms')
def load():
    rooms = Room.query.all()
    return render_template('rooms.html', title='部屋', rooms=rooms)

@rooms.route('/rooms/create')
def create():
    return render_template('create_room.html')