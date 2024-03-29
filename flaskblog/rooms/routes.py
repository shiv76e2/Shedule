from flask import redirect, render_template, url_for, flash, request, Blueprint
from flask_login import current_user
from flaskblog import db
from flaskblog.models import Organizations, OrganizationsResourcesOwnership, Reservations, Resources, OrganizationsUsersBelonging
from flaskblog.rooms.forms import RoomForm
from flaskblog.rooms.dtos import ResourceDto
from flaskblog.rooms.rooms_service import RoomsService

rooms = Blueprint('rooms', __name__)


@rooms.route('/rooms')
def load():
    if not current_user.is_authenticated:
        return redirect(url_for('users.login'))
    rooms = RoomsService.search_available_rooms(current_user.id)
    return render_template('rooms.html', title='部屋', rooms=rooms)

@rooms.route('/rooms/new', methods=['GET', 'POST'])
def new_room():
    form = RoomForm()
    #POST
    if form.validate_on_submit():
        #TODO: capacity To SelectedField
        room = Resources(name=form.name.data, capacity=form.capacity.data)
        #TODO: セッション管理
        db.session.add(room)
        db.session.commit()
        ownership = OrganizationsResourcesOwnership(organization_id=form.organization.data, resource_id = room.id)
        db.session.add(ownership)
        db.session.commit()
        flash('Your room has been created!', 'success')
        return redirect(url_for('rooms.load'))
    #GET
    belongings = OrganizationsUsersBelonging.query.filter_by(user_id = current_user.id)
    if belongings == None:
        return redirect(url_for('organizations.register'))  
    organization_ids = [belonging.organization_id for belonging in belongings]
    organizations = Organizations.query.filter(Organizations.organization_id.in_(organization_ids))
    form.organization.choices = [(org.organization_id, org.name) for org in organizations]
    return render_template('create_room.html', form=form)

@rooms.route('/rooms/delete/<int:room_id>')
def delete_room(room_id):
    rooms = Resources.query.get_or_404(room_id)
    OrganizationsResourcesOwnership.query.filter_by(resource_id=room_id).delete()
    Reservations.query.filter_by(resource_id=room_id).delete()
  
    db.session.delete(rooms)
    db.session.commit()
    
    flash('削除に成功しました。', 'success')
    return redirect(url_for('rooms.load'))