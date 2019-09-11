import os
from flask import current_app, Blueprint, render_template, request, url_for, session, redirect
from decorators.hasPermission import login_required

homeBP = Blueprint('home', __name__, url_prefix='/', template_folder='templates/', static_folder='static/')

@homeBP.route('/')
@login_required
def index():
    return render_template('home.html'), 200
