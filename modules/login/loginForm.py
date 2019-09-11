from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField(
        'Login',
        validators = [
            DataRequired(message="Campo obrigatório")
        ],
        render_kw = {
            'placeholder':'Login'
        }
    )

    password = PasswordField(
        'Senha',
        validators = [DataRequired(message="Campo obrigatório")],
        render_kw = {
            'placeholder':'Senha'
        }
    )