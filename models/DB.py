import pymysql

class DB():
    def __init__(self):
        host = 'localhost'
        user = 'root'
        password = ''
        db = 'product_order'
        self.conexao = pymysql.connect(host, user, password, db)