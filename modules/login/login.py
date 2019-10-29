from flask import current_app, Blueprint, render_template, request, url_for, redirect, session, flash
from .loginForm import LoginForm
from models.Client import Client
from app import bcrypt

loginBP = Blueprint('login', __name__, url_prefix='/login', template_folder='templates/', static_folder='static/')

@loginBP.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = Client()
        user.getByLogin(form.login.data)
        if not user.id:
            flash('Credenciais inválidas')
            return redirect( url_for('login.index') )
        if bcrypt.check_password_hash(user.senha, form.password.data):
            session.clear()
            session.permanent = True
            session['user_id'] = user.id
            session['user_nome'] = user.nome
            session['user_login'] = user.login
            session['user_grupo'] = user.grupo
            return redirect( url_for('home.index') )
        else:
            flash('Credenciais inválidas')

    return render_template('login.html', form=form), 200

@loginBP.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id')
    session.pop('user_nome')
    session.pop('user_login')
    session.pop('user_grupo')
    session.clear()
    return redirect( url_for('login.index') )
