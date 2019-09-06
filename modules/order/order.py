import os
from flask import current_app, Blueprint, render_template, request, url_for

orderBP = Blueprint('order', __name__, url_prefix='/order', template_folder='templates/', static_folder='static/')

@orderBP.route('/')
def index():
    return render_template('order.html'), 200

@orderBP.route('/add')
def add():
    return render_template('order_add.html'), 200
