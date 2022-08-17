from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from flaskblog import db, bcrypt
from flaskblog.organizations.forms import OrganizationRegistrationForm
from flaskblog.models import Organizations, OrganizationsUsersBelonging, Users


organizations = Blueprint('organizations', __name__)

@organizations.route('/organizations')
def load(): 
    if not current_user.is_authenticated:
        return redirect(url_for('main.home'))
    id = int(current_user.get_id())
    belongings = OrganizationsUsersBelonging.query.filter_by(user_id = id)
    if belongings == None:
        return redirect(url_for('organizations.register'))  
    organization_ids = [belonging.organization_id for belonging in belongings]
    organizations = Organizations.query\
                                                .filter(Organizations.organization_id.in_(organization_ids))\
                                                .join(Users, Organizations.owner_id == Users.id)\
                                                .all()
    #TODO: TEAM所有者の名前表示     
    
    
    return render_template('teams.html', organizations = organizations)


@organizations.route("/organizations/register", methods=['GET', 'POST'])
def register():
    form = OrganizationRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        owner_id = int(current_user.get_id())
        organization = Organizations(organization_id=form.organization_id.data, name=form.name.data, password=hashed_password, owner_id = owner_id)
        db.session.add(organization)
        belonging = OrganizationsUsersBelonging(organization_id=form.organization_id.data, user_id=owner_id)
        db.session.add(belonging)
        db.session.commit()
        flash('TEAMの作成が完了しました。', 'success')
        return redirect(url_for('main.home'))
    return render_template('register/organization_register.html', title="TEAM", form = form)

#TODO: TEAM脱退
@organizations.route("/organizations/leave/<string:organization_id>")
def leave(organization_id):
    #TODO: get_or_404
    #organization = Organizations.query.get_or_404(organization_id)
    #mappingを消す
    OrganizationsUsersBelonging.query.filter_by(organization_id = organization_id)\
                                                        .filter_by(user_id = current_user.id)\
                                                        .delete()
    db.session.commit()
    flash('TEAMを脱退しました。', 'success')
    return(redirect(url_for('organizations.load')))

@organizations.route('/organizations/search', methods=['GET', 'POST'])
def search():
    return render_template('search_organization_form.html', title="TEAM")

