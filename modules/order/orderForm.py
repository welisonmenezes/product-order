from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import Length

class OrderForm(FlaskForm):
    cliente = HiddenField()

    order_id = HiddenField()

    observacao = StringField(
        'Observação',
        validators = [
            Length(min=0, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Observação'
        }
    )