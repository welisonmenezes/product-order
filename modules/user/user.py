import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect
from .userForm import UserForm
from decorators.hasPermission import login_required
from models.User import User
from app import bcrypt

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
    title = 'Cadastrar usuário'
    form = UserForm(request.form)
    if form.validate_on_submit():
        user = User(
            form.nome.data,
            form.login.data,
            bcrypt.generate_password_hash(form.senha.data),
            form.grupo.data
        )
        ret = user.insert()
        flash(ret, 'info')
        return redirect(url_for('user.edit', id=user.id))
    return render_template('user_form.html', form=form, title=title), 200


@userBP.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    title = 'Editar Usuário'
    user = User()
    ret = user.get(id)
    if not user.id:
        flash(ret, 'info')
        return redirect(url_for('user.index'))

    if request.form:
        form = UserForm()
        user.nome = form.nome.data
        user.login = form.login.data
        user.grupo = form.grupo.data
        if form.senha.data != '':
            user.senha = bcrypt.generate_password_hash(form.senha.data)
    else:
        form = UserForm()
        form.nome.data = user.nome
        form.login.data = user.login
        form.grupo.data = user.grupo
    
    form.senha.validators = []
    if form.validate_on_submit():
        ret = user.update()
        flash(ret, 'info')
        return redirect(url_for('user.edit', id=user.id))
    return render_template('user_form.html', form=form, title=title, userId=id), 200


@userBP.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    user = User()
    ret = user.get(id)
    if not user.id:
        flash(ret, 'info')
        return redirect(url_for('user.index'))
    if request.method == 'POST':
        ret = user.delete()
        flash(ret, 'info')
        return redirect(url_for('user.index'))
    title = 'Deseja realmente deletar o usuário ' + user.nome + '?'
    return render_template('user_delete.html', userId=id, title=title), 200