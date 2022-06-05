from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flaskblog.models import Organizations

class OrganizationRegistrationForm(FlaskForm):
    name = StringField('名称',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('参加パスワード', validators=[DataRequired()])
    confirm_password = PasswordField('参加パスワード確認',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('作成')
    
    def validate_username(self, name):
        user = Organizations.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('That name is taken. Please choose a different one.')
    
