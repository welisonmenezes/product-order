from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email

class NonValidatingSelectField(SelectField):
    def pre_validate(self, form):
        pass

class ClientForm(FlaskForm):
    
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