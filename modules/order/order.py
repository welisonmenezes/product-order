import os
from flask import current_app, Blueprint, render_template, request, url_for
from .orderForm import OrderForm
from decorators.hasPermission import login_required

orderBP = Blueprint('order', __name__, url_prefix='/order', template_folder='templates/', static_folder='static/')

@orderBP.route('/')
@login_required
def index():
    return render_template('order.html'), 200

@orderBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = OrderForm(request.form)
    if form.validate_on_submit():
        print('valido')
    return render_template('order_add.html', form=form), 200
