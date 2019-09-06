import os
from flask import current_app, Blueprint, render_template, request, url_for

authBP = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')

@authBP.route('/')
def index():
    return render_template('auth.html'), 200
