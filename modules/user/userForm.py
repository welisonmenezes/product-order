from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length

class UserForm(FlaskForm):
    nome = StringField(
        'Nome',
        validators = [
            DataRequired(message="Campo obrigatório"),
            Length(min=1, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Nome'
        }
    )

    login = StringField(
        'Login',
        validators = [
            DataRequired(message="Campo obrigatório"),
            Length(min=1, max=45, message='É permitido no máximo 45 caracteres')
        ],
        render_kw = {
            'placeholder':'Login'
        }
    )

    senha = PasswordField(
        'Senha',
        validators = [
            DataRequired(message="Campo obrigatório"),
            Length(min=1, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Senha'
        }
    )

    grupo = SelectField(
        'Grupo',
        validators = [
            DataRequired(message="Campo obrigatório"),
            Length(min=1, max=10, message='É permitido no máximo 10 caracteres')
        ],
        choices = [('', 'Selecione'), ('admin', 'Administrador'), ('almoxerife', 'Almoxerife'), ('user', 'Usuário')],
        render_kw = {
            'placeholder':'Grupo'
        }
    )