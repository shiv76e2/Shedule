from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class RoomForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    capacity = IntegerField('Capacity', validators=[DataRequired()])
    organization = SelectField(u'TEAM')
    submit = SubmitField('登録する')
    