import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect, session, jsonify
from wtforms import FieldList, FormField
from .orderForm import OrderForm
from decorators.hasPermission import login_required
from models.Order import Order
from models.OrderProduct import OrderProduct
from datetime import datetime
import copy

orderBP = Blueprint('order', __name__, url_prefix='/order', template_folder='templates/', static_folder='static/')

@orderBP.route('/')
@login_required
def index():
    order = Order()
    orders = order.getAll()
    return render_template('order.html', orders=orders), 200

@orderBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    title = 'Cadastrar Pedido'
    form = OrderForm()
    form.cliente.data = session.get('user_id', '')

    if request.form:
        form = OrderForm(request.form)

        pedidos_produtos = copy.deepcopy(form.pedidos_produtos.data)

        for pp1 in form.pedidos_produtos.data:
            form.pedidos_produtos.pop_entry()
            
        for pp in pedidos_produtos:
            if pp.get('produto') != '' and pp.get('produto') != 'None':
                pp_form = PedidoProdutoForm()
                pp_form.produto.data = str(pp.get('produto'))
                pp_form.quantidade.data = pp.get('quantidade')
                pp_form.valor.data = pp.get('valor')
                pp_form.observacao.data = pp.get('observacao')
                form.pedidos_produtos.append_entry(pp_form.data)

    if form.validate_on_submit():
        now = datetime.now()
        order = Order(
            now.strftime("%y-%m-%d %H:%M:%S"),
            form.observacao.data,
            form.cliente.data
        )
        ret = order.insert()
        if order.id:
            for product in form.pedidos_produtos:
                check_prod = OrderProduct().getByOrderIdAndProductId(order.id, product.produto.data)
                if not check_prod:
                    orderproduct = OrderProduct(
                        order.id,
                        product.produto.data,
                        product.quantidade.data,
                        product.valor.data,
                        product.observacao.data
                    )
                    orderproduct.insert()
        flash(ret, 'info')
        return redirect(url_for('order.edit', id=order.id))
    return render_template('order_form.html', form=form, title=title, mode='add'), 200


@orderBP.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    title = 'Editar Pedido'
    order = Order()
    ret = order.get(id)
    if not order.id:
        flash(ret, 'info')
        return redirect(url_for('order.index'))
    
    if not request.form:
        form = OrderForm()
        form.cliente.data = str(order.clientes_id)
        form.observacao.data = order.observacao
        orderproduct = OrderProduct()
        pedidos_produtos = orderproduct.getByOrderId(order.id)
        if pedidos_produtos:
            form.pedidos_produtos.pop_entry()
            for pedido_produto in pedidos_produtos:
                pp_form = PedidoProdutoForm()
                pp_form.produto.data = str(pedido_produto[1])
                pp_form.quantidade.data = pedido_produto[2]
                pp_form.valor.data = pedido_produto[3]
                pp_form.observacao.data = pedido_produto[4]
                form.pedidos_produtos.append_entry(pp_form.data)
    else:
        form = OrderForm(request.form)

        pedidos_produtos = copy.deepcopy(form.pedidos_produtos.data)

        for pp1 in form.pedidos_produtos.data:
            form.pedidos_produtos.pop_entry()
            
        for pp in pedidos_produtos:
            if pp.get('produto') != '' and pp.get('produto') != 'None':
                pp_form = PedidoProdutoForm()
                pp_form.produto.data = str(pp.get('produto'))
                pp_form.quantidade.data = pp.get('quantidade')
                pp_form.valor.data = pp.get('valor')
                pp_form.observacao.data = pp.get('observacao')
                form.pedidos_produtos.append_entry(pp_form.data)

    if form.validate_on_submit():
        
        order.observacao = form.observacao.data
        order.clientes_id = form.cliente.data
        
        orderproduct = OrderProduct()
        orderproduct.pedidos_id = order.id
        orderproduct.delete()
        for product in form.pedidos_produtos:
            check_prod = OrderProduct().getByOrderIdAndProductId(order.id, product.produto.data)
            if not check_prod:
                orderproduct = OrderProduct(
                    order.id,
                    product.produto.data,
                    product.quantidade.data,
                    product.valor.data,
                    product.observacao.data
                )
                orderproduct.insert()
        ret = order.update()

        flash(ret, 'info')
        return redirect(url_for('order.edit', id=order.id))
    return render_template('order_form.html', form=form, title=title, mode='edit', orderId=order.id), 200


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
    return jsonify({'message': 'teste'})