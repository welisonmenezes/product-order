import os
from flask import current_app, Blueprint, render_template, request, url_for, flash,redirect
from .orderForm import OrderForm
from decorators.hasPermission import login_required
from models.Order import Order
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
                print(product.produto)
        flash(ret, 'info')
        return redirect(url_for('order.add'))
    return render_template('order_form.html', form=form, title=title), 200
