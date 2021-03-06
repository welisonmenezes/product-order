from models.DB import DB

class OrderProduct():

    def __init__(self, pedidos_id=None, produtos_id=None, quatidade=None, valor=None, observacao=''):
        self.id = None
        self.pedidos_id = pedidos_id
        self.produtos_id = produtos_id
        self.quatidade = quatidade
        self.valor = valor
        self.observacao = observacao


    def getByOrderId(self, id_pedido):
        banco=DB()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT pedidos_produtos.pedidos_id, pedidos_produtos.produtos_id, pedidos_produtos.quantidade, pedidos_produtos.valor, pedidos_produtos.observacao, produtos.descricao, produtos.valor, produtos.imagem FROM pedidos_produtos LEFT JOIN produtos ON pedidos_produtos.produtos_id = produtos.id WHERE pedidos_produtos.pedidos_id = %s' , (id_pedido))
            result = c.fetchall()
            c.close()
            return result
        except:
            return None

    
    def getByOrderIdAndProductId(self, id_pedido, id_produto):
        banco=DB()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT pedidos_id, produtos_id, quantidade, valor, observacao FROM pedidos_produtos WHERE pedidos_id = %s AND produtos_id = %s' , (id_pedido, id_produto))
            for linha in c:
                self.pedidos_id=linha[0]
                self.produtos_id=linha[1]
                self.quatidade=linha[2]
                self.valor=linha[3]
                self.observacao=linha[4]
                return True
            c.close()
            return False
        except:
            return False


    def insert(self):
        banco = DB()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO pedidos_produtos(pedidos_id, produtos_id, quantidade, valor, observacao) VALUES (%s, %s, %s, %s, %s)' , (self.pedidos_id, self.produtos_id, self.quatidade, self.valor, self.observacao))
            banco.conexao.commit()
            self.id = c.lastrowid
            c.close()
            return 'Produto do pedido cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do produto do pedido'


    def update(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE pedidos_produtos SET  quantidade = %s, valor = %s, observacao = %s WHERE pedidos_id = %s AND produtos_id = %s' , (self.quatidade, self.valor, self.observacao, self.pedidos_id, self.produtos_id))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do produto do pedido'


    def delete(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM pedidos_produtos WHERE pedidos_id = %s AND produtos_id = %s' , (self.pedidos_id, self.produtos_id))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do produto do pedido'

    
    def deleteByPedido(self, order_id):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM pedidos_produtos WHERE pedidos_id = %s' , (order_id))
            banco.conexao.commit()
            c.close()
            return True
        except:
            return False


    def hasByProduct(self, product_id):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT COUNT(pedidos_id) FROM pedidos_produtos WHERE pedidos_produtos.produtos_id = %s', (product_id))
            result = c.fetchall()
            c.close()
            if result[0][0] > 0:
                return True
            return False
        except:
            return False
