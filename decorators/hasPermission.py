from flask import url_for, redirect, session, flash
from functools import wraps

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        user = session.get('user', None)
        if not user:
            flash('Faça login para acessar')
            return redirect(url_for('login.index'))
        return f(*args, **kwargs)   
    return wrap