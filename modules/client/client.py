import os
from flask import current_app, Blueprint, render_template, request, url_for

clientBP = Blueprint('client', __name__, url_prefix='/client', template_folder='templates', static_folder='static')

@clientBP.route('/')
def index():
    return render_template('client.html'), 200

@clientBP.route('/add')
def add():
    return render_template('client_add.html'), 200
