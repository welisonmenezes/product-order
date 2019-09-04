import os
from flask import current_app, Blueprint, render_template, request, url_for

productBP = Blueprint('product', __name__, url_prefix='/product', template_folder='templates/', static_folder='static/')

@productBP.route('/')
def index():
    return render_template('product.html'), 200
