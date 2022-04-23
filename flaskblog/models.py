from flaskblog import db
from datetime import datetime

class Room(db.Model):
    __tablename__ = "room"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    capacity = db.Column(db.Integer)
    update_time = db.Column(db.DateTime, default=datetime.utcnow)