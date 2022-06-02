from flask import redirect, render_template, url_for, flash, request, Blueprint
from flaskblog import db
from flaskblog.models import Resources
from flaskblog.rooms.forms import RoomForm

rooms = Blueprint('rooms', __name__)


@rooms.route('/rooms')
def load():
    rooms = Resources.query.all()
    return render_template('rooms.html', title='部屋', rooms=rooms)

@rooms.route('/rooms/new', methods=['GET', 'POST'])
def new_room():
    form = RoomForm()
    if form.validate_on_submit():
        room = Resources(name=form.name.data, capacity=form.capacity.data)
        db.session.add(room)
        db.session.commit()
        flash('Your room has been created!', 'success')
        return redirect(url_for('rooms.load'))
    return render_template('create_room.html', form=form)

@rooms.route('/rooms/delete/<int:room_id>')
def delete_room(room_id):
    room = Resources.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    flash('削除に成功しました。', 'success')
    return redirect(url_for('rooms.load'))