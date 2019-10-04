from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FieldList, FormField
from wtforms.validators import DataRequired, Length

class PedidoProdutoForm(FlaskForm):
    quantidade = StringField(
        'Quantidade',
        validators = [
            DataRequired(message="Campo obrigatório"),
            Length(min=0, max=11, message='É permitido no máximo 11 caracteres')
        ],
        render_kw = {
            'placeholder':'Quantidade'
        }
    )

    valor = StringField(
        'Valor',
        validators = [
            Length(min=0, max=11, message='É permitido no máximo 11 caracteres')
        ],
        render_kw = {
            'placeholder':'Valor'
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

    produto = SelectField(
        'Produto',
        validators = [
            DataRequired(message="Campo obrigatório")
        ],
        choices = [('', 'Selecione'), ('1', 'Produto um'), ('2', 'Produto dois'), ('3', 'Produto três')],
        render_kw = {
            'placeholder':'Produto'
        }
    )

class OrderForm(FlaskForm):
    cliente = SelectField(
        'Cliente',
        validators = [
            DataRequired(message="Campo obrigatório")
        ],
        choices = [('', 'Selecione'), ('1', 'Usuário um'), ('2', 'Usuário dois'), ('3', 'Usuário três')],
        render_kw = {
            'placeholder':'Cliente'
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

    pedidos_produtos = FieldList(
        FormField(PedidoProdutoForm),
        min_entries=1
    )