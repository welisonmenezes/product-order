from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class NonValidatingSelectField(SelectField):
    def pre_validate(self, form):
        pass

class ClientForm(FlaskForm):

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
    
    nome = StringField(
        'Nome do cliente',
        validators = [
            DataRequired(message='Campo obrigatório'),
            Length(min=1, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Nome Completo'
        }
    )

    endereco = StringField(
        'Endereço',
        validators = [
            DataRequired(message='Campo obrigatório'),
            Length(min=1, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Endereço'
        }
    )

    numero = IntegerField(
        'Número',
        validators = [],
        render_kw = {
            'placeholder':'Número'
        }
    )

    observacao = StringField(
        'Observação',
        validators = [
            Length(min=0, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Observação'
        }
    )

    cep = StringField(
        'CEP',
        validators = [
            Length(min=0, max=9, message='É permitido no máximo 9 caracteres')
        ],
        render_kw = {
            'placeholder':'CEP'
        }
    )

    bairro = StringField(
        'Bairro',
        validators = [
            DataRequired(message='Campo obrigatório'),
            Length(min=1, max=100, message='É permitido no máximo 100 caracteres')
        ],
        render_kw = {
            'placeholder':'Bairro'
        }
    )

    cidade = NonValidatingSelectField(
        'Cidade',
        validators = [
            DataRequired(message='Campo obrigatório'),
            Length(min=1, max=45, message='É permitido no máximo 45 caracteres')
        ],
        choices=[]
    )

    estado = NonValidatingSelectField(
        'Estado',
        validators = [
            DataRequired(message='Campo obrigatório'),
            Length(min=1, max=2, message='É permitido no máximo 2 caracteres')
        ],
        choices=[]
    )

    telefone = StringField(
        'Telefone',
        validators = [
            DataRequired(message='Campo obrigatório'),
            Length(min=1, max=15, message='É permitido no máximo 15 caracteres')
        ],
        render_kw = {
            'placeholder':'Telefone'
        }
    )

    email = StringField(
        'E-mail',
        validators = [
            Length(min=0, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'E-mail'
        }
    )