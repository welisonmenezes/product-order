import os
from flask import current_app, Blueprint, render_template, request, url_for
from .clientForm import ClientForm
from decorators.hasPermission import login_required

clientBP = Blueprint('client', __name__, url_prefix='/client', template_folder='templates', static_folder='static')

@clientBP.route('/')
@login_required
def index():
    return render_template('client.html'), 200

@clientBP.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ClientForm(request.form)
    if form.validate_on_submit():
        print('valido')
    return render_template('client_add.html', form=form), 200
