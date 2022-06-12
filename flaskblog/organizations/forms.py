from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError, Regexp
from flaskblog.models import Organizations

class OrganizationRegistrationForm(FlaskForm):
    organization_id = StringField('id', 
                                    validators=[DataRequired(), Regexp('^[0-9a-zA-Z]*$', 0, "半角英数で入力"), Length(min=2, max=30)])
    name = StringField('名称',
                        validators=[DataRequired(), Length(min=2, max=40)])
    password = PasswordField('参加パスワード', 
                            validators=[DataRequired()])
    confirm_password = PasswordField('参加パスワード確認',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('作成')
    
    def validate_organization_id(self, organization_id):
        user = Organizations.query.filter_by(organization_id=organization_id.data).first()
        if user:
            raise ValidationError('That id is taken. Please choose a different one.')
    
