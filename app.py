from flask import Flask, render_template, redirect, url_for
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_pyfile('config.py')
bcrypt = Bcrypt(app)

# import blueprints
from modules.home.home import homeBP
from modules.error.error import errorBP
from modules.client.client import clientBP
from modules.order.order import orderBP
from modules.product.product import productBP
from modules.login.login import loginBP

# registra blueprints
app.register_blueprint(errorBP)
app.register_blueprint(homeBP)
app.register_blueprint(clientBP)
app.register_blueprint(orderBP)
app.register_blueprint(productBP)
app.register_blueprint(loginBP)

if __name__ == "__main__":
    app.run()