import os
from flask import current_app, Blueprint, render_template, request, url_for

errorBP = Blueprint('error', __name__, url_prefix='/error', template_folder='templates/', static_folder='static/')

@errorBP.route('/404')
def index():
    return render_template('error404.html'), 200

@errorBP.route('/500')
def serverError():
    return render_template('error500.html'), 200
