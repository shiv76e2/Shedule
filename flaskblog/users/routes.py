from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import current_user
from flaskblog import db, bcrypt
from flaskblog.models import User
from flaskblog.users.forms import RegistrationForm


users = Blueprint("users", __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('アカウントの作成が完了しました。', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)