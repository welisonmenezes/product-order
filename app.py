from flask import Flask, render_template, redirect, url_for

from modules.home.home import homeBP
from modules.error.error import errorBP
from modules.client.client import clientBP
from modules.order.order import orderBP
from modules.product.product import productBP

def create_app():
    app = Flask(__name__)

    # config app
    app.config.from_pyfile('config.py')
    
    # blueprint test
    app.register_blueprint(homeBP)
    app.register_blueprint(errorBP)
    app.register_blueprint(clientBP)
    app.register_blueprint(orderBP)
    app.register_blueprint(productBP)

    # @app.errorhandler(404)
    # def nao_encontrado(error):
    #     return redirect('/error', code=302)

    return app