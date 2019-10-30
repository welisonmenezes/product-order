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