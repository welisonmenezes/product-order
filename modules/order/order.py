import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect, session, jsonify
from wtforms import FieldList, FormField
from .orderForm import OrderForm
from decorators.hasPermission import login_required
from models.Order import Order
from models.Client import Client
from models.OrderProduct import OrderProduct
from datetime import datetime
import copy
from base64 import b64encode

orderBP = Blueprint('order', __name__, url_prefix='/order', template_folder='templates/', static_folder='static/')

@orderBP.route('/')
@login_required
def index():
    order = Order()
    user_id = request.args.get('user', None)
    client = Client()
    clients = client.getAll()

    if user_id:
        orders = order.getByUser(user_id)
    else:
        orders = order.getAll()

    return render_template('order.html', orders=orders, clients=clients), 200

@orderBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    title = 'Cadastrar Pedido'
    form = OrderForm()
    form.cliente.data = session.get('user_id', '')

    if request.form:
        form = OrderForm(request.form)

    if form.validate_on_submit():
        if form.order_id.data:
            order = Order()
            ret = order.get(form.order_id.data)
            order.observacao = form.observacao.data
            order.clientes_id = form.cliente.data
            ret = order.update()
            flash(ret, 'info')
            return redirect(url_for('order.index'))
        else:
            flash('É necessário ao menos um produto para cadastrar um pedido.', 'danger')
            
    return render_template('order_form.html', form=form, title=title, mode='add', pageOrigin='add-page'), 200


@orderBP.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    title = 'Editar Pedido'
    order = Order()
    ret = order.get(id)
    if not order.id:
        flash(ret, 'info')
        return redirect(url_for('order.index'))

    order_p = OrderProduct()
    products = order_p.getByOrderId(order.id)
    images = []
    for product in products:
        images.append(b64encode(product[7]).decode("utf-8"))
    
    if not request.form:
        form = OrderForm()
        form.cliente.data = str(order.clientes_id)
        form.observacao.data = order.observacao
        form.order_id.data = order.id
        orderproduct = OrderProduct()
        pedidos_produtos = orderproduct.getByOrderId(order.id)
    else:
        form = OrderForm(request.form)

    if form.validate_on_submit():
        
        order.observacao = form.observacao.data
        order.clientes_id = form.cliente.data
        ret = order.update()
        flash(ret, 'info')
        return redirect(url_for('order.edit', id=order.id))
    return render_template('order_form.html', form=form, title=title, mode='edit', orderId=order.id, clientName=order.cliente_name, pageOrigin='edit-page', products=products, images=images), 200


@orderBP.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    order = Order()
    ret = order.get(id)
    if not order.id:
        flash(ret, 'info')
        return redirect(url_for('order.index'))
    if request.method == 'POST':
        ret = order.delete()
        flash(ret, 'info')
        return redirect(url_for('order.index'))
    title = 'Deseja realmente deletar o pedido ' + str(order.id) + '?'
    return render_template('order_delete.html', orderId=id, title=title), 200


@orderBP.route('/add-order', methods=['POST'])
@login_required
def add_order():
    if (request.form['client']):
        now = datetime.now()
        order = Order(
            now.strftime("%y-%m-%d %H:%M:%S"),
            request.form['obs'],
            request.form['client']
        )
        ret = order.insert()
        if ret == 'Pedido cadastrado com sucesso!':
            return jsonify({'order_id': order.id})
        else:
            return jsonify({'message': ret})
    return jsonify({'message': 'O parâmetro ID do cliente é obrigatório'})


@orderBP.route('/add-product-order', methods=['POST'])
@login_required
def add_product_order():
    if (request.form['pedidos_id']):
        has_product_order = OrderProduct()
        if has_product_order.getByOrderIdAndProductId(request.form['pedidos_id'], request.form['produtos_id']):
            return jsonify({'message': 'Este produto já foi cadastrado neste pedido'})
        order = OrderProduct(
            request.form['pedidos_id'],
            request.form['produtos_id'],
            request.form['quantidade'],
            request.form['valor'],
            request.form['observacao']
        )
        ret = order.insert()
        if ret == 'Produto do pedido cadastrado com sucesso!':
            return jsonify({'pedidos_id': order.pedidos_id, 'produtos_id': order.produtos_id})
        else:
            return jsonify({'message': ret})
    return jsonify({'message': 'Os dados do produto estão incompletos'})


@orderBP.route('/delete-product-order', methods=['POST'])
@login_required
def delete_product_order():
    if (request.form['order_id'] and request.form['product_id']):
        order_p = OrderProduct()
        order_p.pedidos_id = request.form['order_id']
        order_p.produtos_id = request.form['product_id']
        ret = order_p.delete()

        if (request.form['from'] and request.form['from'] == 'add-page'):
            order = Order()
            order.id = request.form['order_id']
            order.delete()

        return jsonify({'message': ret})
    return jsonify({'message': 'O parâmetro ID do pedido e ID do produto são obrigatórios'})



@orderBP.route('/edit-product-order', methods=['POST'])
@login_required
def edit_product_order():
    if (request.form['order_id'] and request.form['product_id']):
        order_p = OrderProduct()
        order_p.pedidos_id = request.form['order_id']
        order_p.produtos_id = request.form['product_id']
        order_p.quatidade = request.form['quantidade']
        order_p.observacao = request.form['observacao']
        order_p.valor = request.form['valor']
        ret = order_p.update()
        return jsonify({'message': ret})
    return jsonify({'message': 'O parâmetro ID do pedido e ID do produto são obrigatórios'})