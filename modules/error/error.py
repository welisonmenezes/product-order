import os
from flask import current_app, Blueprint, render_template, request, url_for

errorBP = Blueprint('error', __name__, url_prefix='/', template_folder='templates/', static_folder='static/')

@errorBP.errorhandler(404)
def notFound(error):
    return render_template('error404.html'), 404

@errorBP.errorhandler(500)
def serverError(error):
    return render_template('error500.html'), 500
