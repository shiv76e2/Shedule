from flask import redirect, render_template, url_for, flash, request, Blueprint
from flaskblog import db
from flaskblog.models import Room
from flaskblog.rooms.forms import RoomForm

rooms = Blueprint('rooms', __name__)


@rooms.route('/rooms')
def load():
    rooms = Room.query.all()
    return render_template('rooms.html', title='部屋', rooms=rooms)

@rooms.route('/rooms/new', methods=['GET', 'POST'])
def new_room():
    form = RoomForm()
    if form.validate_on_submit():
        flash('Your room has been created!', 'success')
        room = Room(name=form.name.data, capacity=form.capacity.data)
        db.session.add(room)
        db.session.commit()
        return redirect(url_for('rooms.load'))
    return render_template('create_room.html', form=form)