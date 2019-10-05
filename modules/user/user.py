import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect
from .userForm import UserForm
from decorators.hasPermission import login_required
from models.User import User

userBP = Blueprint('user', __name__, url_prefix='/user', template_folder='templates', static_folder='static')

@userBP.route('/')
@login_required
def index():
    user = User()
    users = user.getAll()
    return render_template('user.html', users=users), 200

@userBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = UserForm(request.form)
    if form.validate_on_submit():
        user = User(
            form.nome.data,
            form.login.data,
            form.senha.data,
            form.grupo.data
        )
        ret = user.insert()
        flash(ret, 'info')
        return redirect(url_for('user.add'))
    return render_template('user_form.html', form=form), 200
