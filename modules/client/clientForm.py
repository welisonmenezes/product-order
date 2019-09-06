from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange

class ClientForm(FlaskForm):
    codigo = StringField(
        'Código',
        validators = [
            DataRequired(message="Campo obrigatório")
        ],
        render_kw = {
            'placeholder':'Código'
        }
    )

    nome = StringField(
        'Nome do cliente',
        validators = [DataRequired(message="Campo obrigatório")],
        render_kw = {
            'placeholder':'Nome do cliente'
        }
    )

    def validate_codigo(form, field):
        try:
            float(field.data)
        except:
            raise ValidationError('Apenas número')