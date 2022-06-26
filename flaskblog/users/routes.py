from flask import render_template, redirect, url_for, flash, request, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from flaskblog import db, bcrypt
from flaskblog.models import Users, Organizations, OrganizationsUsersBelonging
from flaskblog.users.forms import RegistrationForm, LoginForm


users = Blueprint("users", __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = Users(name=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('アカウントの作成が完了しました。', 'success')
        return redirect(url_for('users.login'))
    return render_template('register/user_register.html', title='Register', form=form)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/account")
@login_required
def account():
    user_id = current_user.id
    #所属: 
    belongings = OrganizationsUsersBelonging.query.filter_by(user_id = current_user.id)
    if belongings == None:
        return redirect(url_for('organizations.register'))  

    organization_ids = [belonging.organization_id for belonging in belongings]
    organizations = Organizations.query.filter(Organizations.organization_id.in_(organization_ids))
    return render_template('account.html', title='アカウント', organizations = organizations)