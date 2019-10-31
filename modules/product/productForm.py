from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, SubmitField, FileField, FloatField
from wtforms.validators import DataRequired, Length
from werkzeug.utils import secure_filename

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
            DataRequired(message="Campo obrigatório. (Apenas valor numérico)")
        ],
        render_kw = {
            'placeholder':'Valor'
        }
    )

    imagem = FileField(
        'Imagem',
        validators = [
            FileRequired(message="Imagem obrigatória"),
            FileAllowed(['jpg', 'png', 'jpeg', 'gif'], "Apenas imagens é permitido")
        ]
    )

    imagem_edicao = FileField(
        'Trocar Imagem',
        validators = [
            FileAllowed(['jpg', 'png', 'jpeg', 'gif'], "Apenas imagens é permitido")
        ]
    )

    submit = SubmitField('Salvar')