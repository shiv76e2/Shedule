from flaskblog import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Room(db.Model):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    capacity = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)



class Resources(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    
    organizations_users_belonging = db.relationship("Organizations_Users_Belonging", backref="resources", lazy=True)
    reservations = db.relationship("Reservations", backref="resources", lazy=True)
    organizations_resources_ownership = db.relationship("Organizations_Resources_Ownership", backref="resources", lazy=True)
    

class Users(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
    
    reservations = db.relationship("Reservations", backref="users", lazy=True)
    organizations = db.relationship("Organizations", backref="users", lazy=True)
    organizations_users_belonging = db.relationship("Organizations_Users_Belonging", backref="users", lazy=True)

    
class Organizations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)

    organizations_resources_ownership = db.relationship("Organizations_Resources_Ownership", backref="organizations", lazy=True)


class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey("resources.id"), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) 
    update_time = db.Column(db.DateTime, default=datetime.utcnow)


class Organizations_Users_Belonging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey("resources.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)


class Organizations_Resources_Ownership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey("organizations.id"), nullable=False)
    resource_id = db.Column(db.Integer, db.ForeignKey("resources.id"), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)
