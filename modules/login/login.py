from flask import current_app, Blueprint, render_template, request, url_for

loginBP = Blueprint('login', __name__, url_prefix='/login', template_folder='templates/', static_folder='static/')

@loginBP.route('/')
def index():
    return render_template('login.html'), 200
