import os
from flask import current_app, Blueprint, render_template, request, url_for
from .userForm import UserForm
from decorators.hasPermission import login_required

userBP = Blueprint('user', __name__, url_prefix='/user', template_folder='templates', static_folder='static')

@userBP.route('/')
@login_required
def index():
    return render_template('user.html'), 200

@userBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = UserForm(request.form)
    if form.validate_on_submit():
        print('valido')
    return render_template('user_add.html', form=form), 200
