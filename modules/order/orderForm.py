from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FieldList, FormField
from wtforms.validators import DataRequired, Length

from models.Client import Client
clients = Client().getAll()
client_choices = [('', 'Selecione')]
if clients:
    for client in clients:
        client_choices.append((str(client[0]), client[1]))


from models.Product import Product
products = Product().getAll()
product_choices = [('', 'Selecione')]
if products:
    for product in products:
        product_choices.append((str(product[0]), product[1]))


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
        choices = product_choices,
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
        choices = client_choices,
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