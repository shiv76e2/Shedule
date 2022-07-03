from flask import Blueprint, render_template
from flaskblog.models import Reservations
from flaskblog.reservations.forms import ReservationForm

reservations = Blueprint('reservations',  __name__)

@reservations.route('/reservations/new', methods=['GET', 'POST'])
def new_reservation():
    form = ReservationForm()
    return render_template('register/reservation_register.html', form=form)