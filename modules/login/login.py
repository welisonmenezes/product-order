from flask import current_app, Blueprint, render_template, request, url_for, redirect, session, flash
from .loginForm import LoginForm

loginBP = Blueprint('login', __name__, url_prefix='/login', template_folder='templates/', static_folder='static/')

@loginBP.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        if (request.form.get('login') == 'abc' and request.form.get('password') == 'bolinhas'):
            session.clear()
            session.permanent = True
            session['user'] = request.form.get('login')
            return redirect( url_for('home.index') )
        else:
            flash('Credenciais inválidas')
    return render_template('login.html', form=form), 200

@loginBP.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user')
    session.clear()
    return redirect( url_for('login.index') )
