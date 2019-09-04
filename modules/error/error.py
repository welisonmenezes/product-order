import os
from flask import current_app, Blueprint, render_template, request, url_for

errorBP = Blueprint('error', __name__, url_prefix='/error', template_folder='templates', static_folder='static')

@errorBP.route('/')
def index():
    return render_template('error.html'), 200
