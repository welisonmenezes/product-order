import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect
from .productForm import ProductForm
from models.Product import Product
from decorators.hasPermission import login_required

productBP = Blueprint('product', __name__, url_prefix='/product', template_folder='templates/', static_folder='static/')

@productBP.route('/')
@login_required
def index():
    return render_template('product.html'), 200

@productBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ProductForm()
    title = 'Cadastrar produto'
    if form.validate_on_submit():
        image = request.files.get('imagem')
        if image:
            product = Product(
                form.descricao.data,
                form.valor.data,
                image.read()
            )
            ret = product.insert()
            flash(ret, 'info')
            return redirect(url_for('product.add'))
    return render_template('product_form.html', form=form, title=title), 200