from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Length

class ProductForm(FlaskForm):
    descricao = StringField(
        'Descrição',
        validators = [
            DataRequired(message="Campo obrigatório"),
            Length(min=1, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Descrição'
        }
    )

    valor = StringField(
        'Valor',
        validators = [
            DataRequired(message="Campo obrigatório"),
            Length(min=1, max=11, message='É permitido no máximo 11 caracteres')
        ],
        render_kw = {
            'placeholder':'Valor'
        }
    )

    imagem = FileField(
        'Imagem',
        validators = [
            DataRequired(message="Campo obrigatório")
        ],
        render_kw = {
            'placeholder':'Senha'
        }
    )