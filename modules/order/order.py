import os
from flask import current_app, Blueprint, render_template, request, url_for, flash,redirect
from wtforms import FieldList, FormField
from .orderForm import OrderForm, PedidoProdutoForm
from decorators.hasPermission import login_required
from models.Order import Order
from models.OrderProduct import OrderProduct
from datetime import datetime

orderBP = Blueprint('order', __name__, url_prefix='/order', template_folder='templates/', static_folder='static/')

@orderBP.route('/')
@login_required
def index():
    return render_template('order.html'), 200

@orderBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    title = 'Cadastrar Pedido'
    form = OrderForm(request.form)

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
        return redirect(url_for('order.add'))
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

    if form.validate_on_submit():
        print('legal')
        #ret = order.update()
        #flash(ret, 'info')
        #return redirect(url_for('order.edit', id=product.id))
    return render_template('order_form.html', form=form, title=title, mode='edit'), 200