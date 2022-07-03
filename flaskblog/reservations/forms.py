from lzma import FORMAT_ALONE
from flask_wtf import FlaskForm
from wtforms import DateTimeField, SubmitField
from wtforms.fields.html5 import DateField, TimeField
from wtforms.validators import DataRequired

class ReservationForm(FlaskForm):
    start_date = DateField('開始日', format='%Y=%m-%d', validators=[DataRequired()])
    start_time = TimeField('開始時間', validators=[DataRequired()])
    end_date = DateField('終了日', format='%Y=%m-%d', validators=[DataRequired()])
    end_time = TimeField('終了時間', validators=[DataRequired()])
    submit = SubmitField('登録する')