import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect
from .clientForm import ClientForm
from decorators.hasPermission import login_required
from models.Client import Client

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
        client = Client(
            form.nome.data,
            form.endereco.data,
            form.numero.data,
            form.observacao.data,
            form.cep.data,
            form.bairro.data,
            form.cidade.data,
            form.estado.data,
            form.telefone.data,
            form.email.data,
        )
        ret = client.insert()
        flash(ret, 'info')
        return redirect(url_for('client.add'))
    return render_template('client_form.html', form=form, title=title), 200
