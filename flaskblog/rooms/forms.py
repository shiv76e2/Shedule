from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired

class RoomForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    capacity = IntegerField('Capacity', validators=[DataRequired()])
    organization = SelectField(u'TEAM', validate_choice=False, coerce=str)
    submit = SubmitField('登録する')
    