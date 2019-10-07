import os
from flask import current_app, Blueprint, render_template, request, url_for
from .clientForm import ClientForm
from decorators.hasPermission import login_required

clientBP = Blueprint('client', __name__, url_prefix='/client', template_folder='templates', static_folder='static')

@clientBP.route('/')
@login_required
def index():
    return render_template('client.html'), 200

@clientBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    title = 'Cadastrar Cliente'
    form = ClientForm(request.form)

    if form.estado.data != 'None':
        form.estado.choices = [(form.estado.data, form.estado.data)]

    if form.cidade.data != 'None':
        form.cidade.choices = [(form.cidade.data, form.cidade.data)]

    if form.validate_on_submit():
        print('valido')
    return render_template('client_add.html', form=form, title=title), 200
