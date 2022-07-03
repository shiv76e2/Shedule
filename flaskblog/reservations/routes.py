from datetime import datetime
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user
from flaskblog import db
from flaskblog.models import Reservations, Resources
from flaskblog.reservations.forms import ReservationForm
from flaskblog.rooms.rooms_service import RoomsService

reservations = Blueprint('reservations',  __name__)

@reservations.route('/reservations/new', methods=['GET', 'POST'])
def new_reservation():
    form = ReservationForm()
    #POST
    if form.validate_on_submit():
        
        #TODO: 人数指定
        room = Resources.query.filter_by(id = form.rooms.data).all()[0]
        sd = form.start_date.data
        st = form.start_time.data
        ed = form.end_date.data
        et = form.end_time.data
        capa = room.capacity
        start_datetime = datetime(sd.year, sd.month, sd.day, st.hour, st.minute, st.second)
        end_datetime = datetime(ed.year, ed.month, ed.day, et.hour, st.minute, et.second)
        reservation = Reservations(resource_id = form.rooms.data,
                                                amount = capa,
                                                start_time = start_datetime,
                                                end_time = end_datetime,
                                                user_id = current_user.id)
        db.session.add(reservation)
        db.session.commit()
        return render_template('register/reservation_register.html', form=form)    

    #GET
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    rooms = RoomsService.search_available_rooms(current_user.id)
    form.rooms.choices = [(room.id, room.name + " / " + room.organizations_resources_ownership[0].organizations.name) for room in rooms]
    return render_template('register/reservation_register.html', form=form)