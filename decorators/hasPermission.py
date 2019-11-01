from flask import url_for, redirect, session, flash
from functools import wraps

# senha para iniciar
# $2b$12$HLmXrD04OduCBeqEqW9Cje69DVAXdhie6E7Ts7RAEthit.te7uxwu (123456)

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        user = session.get('user_login', None)
        if not user:
            flash('Faça login para acessar')
            return redirect(url_for('login.index'))
        return f(*args, **kwargs)   
    return wrap


def must_be_admin(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        grupo = session.get('user_grupo', None)
        if not grupo or grupo != 'admin':
            flash('Você não tem permissão para este recurso')
            return redirect(url_for('home.index'))
        return f(*args, **kwargs)   
    return wrap

def if_user_bye(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        grupo = session.get('user_grupo', None)
        if not grupo or grupo == 'user':
            flash('Você não tem permissão para este recurso')
            return redirect(url_for('home.index'))
        return f(*args, **kwargs)   
    return wrap