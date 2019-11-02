import os
from flask import current_app, Blueprint, render_template, request, url_for, flash, redirect, jsonify
from .productForm import ProductForm
from models.Product import Product
from models.OrderProduct import OrderProduct
from decorators.hasPermission import login_required, if_user_bye
from base64 import b64encode

productBP = Blueprint('product', __name__, url_prefix='/product', template_folder='templates/', static_folder='static/')

@productBP.route('/')
@login_required
def index():
    product = Product()
    desc = request.args.get('descricao', None)

    if desc:
        products = product.getByDesc(desc)
    else:
        products = product.getAll()

    images = []
    for product in products:
        images.append(b64encode(product[3]).decode("utf-8"))
    return render_template('product.html', products=products, images=images, desc=desc), 200


@productBP.route('/add', methods=['GET', 'POST'])
@login_required
@if_user_bye
def add():
    form = ProductForm()
    title = 'Cadastrar Produto'
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
            return redirect(url_for('product.index'))
    return render_template('product_form.html', form=form, title=title, mode='add'), 200


@productBP.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
@if_user_bye
def edit(id):
    title = 'Editar Produto'
    product = Product()
    ret = product.get(id)
    if not product.id:
        flash(ret, 'info')
        return redirect(url_for('product.index'))
    
    image = b64encode(product.imagem).decode("utf-8")
    if request.form:
        form = ProductForm()
        product.descricao = form.descricao.data
        product.valor = form.valor.data
        if form.imagem_edicao.data.filename != '':
            image_edit = request.files.get('imagem_edicao')
            product.imagem = image_edit.read()
        else:
            image_edit = product.imagem
    else:
        form = ProductForm()
        form.descricao.data = product.descricao
        form.valor.data = product.valor

    form.imagem.validators = []
    if form.validate_on_submit():
        ret = product.update()
        flash(ret, 'info')
        return redirect(url_for('product.edit', id=product.id))
    return render_template('product_form.html', form=form, title=title, mode='edit', image=image, productId=product.id), 200


@productBP.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
@if_user_bye
def delete(id):
    product = Product()
    ret = product.get(id)
    if not product.id:
        flash(ret, 'info')
        return redirect(url_for('product.index'))

    order = OrderProduct()
    has = order.hasByProduct(id)
    if has:
        flash('O produto não pode ser deletado pois ele já está relacionado à algum pedido.', 'info')
        return redirect(url_for('product.index'))

    if request.method == 'POST':
        ret = product.delete()
        flash(ret, 'info')
        return redirect(url_for('product.index'))
    title = 'Deseja realmente deletar o produto ' + str(product.id) + '?'
    return render_template('product_delete.html', productId=id, title=title), 200


@productBP.route('/search-prod/<prod>', methods=['GET'])
@login_required
def search_prod(prod):
    product = Product()
    products = product.filterByName(prod)
    ret_prods = []
    if products:
        for p in products:
            img = str(b64encode(p[3]).decode("utf-8"))
            ret_prods.append({"id": p[0], "descricao": p[1], "valor": str(p[2]), "imagem": img})
    return jsonify(ret_prods)
