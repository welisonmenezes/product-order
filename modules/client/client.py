import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect
from .clientForm import ClientForm
from decorators.hasPermission import login_required
from app import bcrypt
from models.Client import Client
from utils.estados import estados

clientBP = Blueprint('client', __name__, url_prefix='/client', template_folder='templates', static_folder='static')

@clientBP.route('/')
@login_required
def index():
    client = Client()
    clients = client.getAll()
    return render_template('client.html', clients=clients), 200


@clientBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    title = 'Cadastrar Usuário'
    form = ClientForm(request.form)
    
    if form.estado.data != 'None':
        form.estado.choices = [(form.estado.data, estados[form.estado.data])]

    if form.cidade.data != 'None':
        form.cidade.choices = [(form.cidade.data, form.cidade.data)]
        
    if form.validate_on_submit():
        cliente_ = Client()
        cliente_.getByLogin(form.login.data)
        if cliente_.id:
            flash('O login informado já existe na base de dados', 'warning')
        else:
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
                form.login.data,
                bcrypt.generate_password_hash(form.senha.data),
                form.grupo.data,
            )
            ret = client.insert()
            flash(ret, 'info')
            return redirect(url_for('client.edit', id=client.id))
    return render_template('client_form.html', form=form, title=title), 200


@clientBP.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    title = 'Editar Usuário'
    client = Client()
    ret = client.get(id)
    if not client.id:
        flash(ret, 'info')
        return redirect(url_for('client.index'))

    if request.form:
        form = ClientForm()
        client.nome = form.nome.data
        client.telefone = form.telefone.data
        client.endereco = form.endereco.data
        client.numero = form.numero.data
        client.cep = form.cep.data
        client.bairro = form.bairro.data
        client.observacao = form.observacao.data
        client.email = form.email.data
        client.cidade = form.cidade.data
        client.estado = form.estado.data
        #client.login = form.login.data
        client.grupo = form.grupo.data
        if form.senha.data != '':
            client.senha = bcrypt.generate_password_hash(form.senha.data)
        
        if form.login.data != client.login:
            cliente_ = Client()
            cliente_.getByLogin(form.login.data)
            if cliente_.id:
                flash('O login informado já existe na base de dados', 'warning')
                return redirect(url_for('client.edit', id=client.id))
            else:
                client.login = form.login.data
    else:
        form = ClientForm()
        form.login.data = client.login
        form.grupo.data = client.grupo
        form.nome.data = client.nome
        form.telefone.data = client.telefone
        form.endereco.data = client.endereco
        form.numero.data = client.numero
        form.cep.data = client.cep
        form.bairro.data = client.bairro
        form.observacao.data = client.observacao
        form.email.data = client.email
        if client.estado:
            form.estado.choices = [(client.estado, estados[client.estado])]
        if client.cidade:
            form.cidade.choices = [(client.cidade, client.cidade)]
    
    form.senha.validators = []
    if form.validate_on_submit():
        ret = client.update()
        flash(ret, 'info')
        return redirect(url_for('client.edit', id=client.id))
    return render_template('client_form.html', form=form, title=title, clientId=id), 200


@clientBP.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    client = Client()
    ret = client.get(id)
    if not client.id:
        flash(ret, 'info')
        return redirect(url_for('client.index'))
    if request.method == 'POST':
        ret = client.delete()
        flash(ret, 'info')
        return redirect(url_for('client.index'))
    title = 'Deseja realmente deletar o usuário ' + client.nome + '?'
    return render_template('client_delete.html', clientId=id, title=title), 200
