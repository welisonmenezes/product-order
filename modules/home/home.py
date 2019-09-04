import os
from flask import current_app, Blueprint, render_template, request, url_for

homeBP = Blueprint('home', __name__, url_prefix='/', template_folder='templates/', static_folder='static/')

@homeBP.route('/')
def index():
    return render_template('home.html'), 200
