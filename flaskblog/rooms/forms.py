from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RoomForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    capacity = IntegerField('Capacity', validators=[DataRequired()])
    submit = SubmitField('登録する')