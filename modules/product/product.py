import os
from flask import current_app, Blueprint, render_template, request, url_for
from .productForm import ProductForm
from decorators.hasPermission import login_required

productBP = Blueprint('product', __name__, url_prefix='/product', template_folder='templates/', static_folder='static/')

@productBP.route('/')
@login_required
def index():
    return render_template('product.html'), 200

@productBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ProductForm(request.form)
    if form.validate_on_submit():
        print('valido')
    return render_template('product_add.html', form=form), 200
