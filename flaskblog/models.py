from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

class Resources(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)

    servations = db.relationship("Reservations", backref="resources", lazy=True)
    organizations_resources_ownership = db.relationship("OrganizationsResourcesOwnership", backref="resources", lazy=True)
    

class Users(db.Model, UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    
    reservations = db.relationship("Reservations", backref="users", lazy=True)
    organizations = db.relationship("Organizations", backref="users", lazy=True)
    organizations_users_belonging = db.relationship("OrganizationsUsersBelonging", backref="users", lazy=True)

    
class Organizations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)

    organizations_users_ownership = db.relationship("OrganizationsUsersBelonging", backref="organizations", lazy=True)
    organizations_resources_ownership = db.relationship("OrganizationsResourcesOwnership", backref="organizations", lazy=True)


class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey("resources.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) 
    update_time = db.Column(db.DateTime, default=datetime.utcnow)


class OrganizationsUsersBelonging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)


class OrganizationsResourcesOwnership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.id"), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey("resources.id"), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
