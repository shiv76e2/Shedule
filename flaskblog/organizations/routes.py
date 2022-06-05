from flask import Blueprint, render_template
from flaskblog.organizations.forms import OrganizationRegistrationForm
from flaskblog.models import Organizations


organizations = Blueprint('organizations', __name__)

@organizations.route('/organizations')
def load():
    form = OrganizationRegistrationForm()
    return render_template('register/organization_register.html', title="TEAM", form = form)