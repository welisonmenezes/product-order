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
            c.execute('SELECT pedidos_id, produtos_id, quantidade, valor, observacao FROM pedidos_produtos WHERE pedidos_id = %s' , (id_pedido))
            result = c.fetchall()
            c.close()
            return result
        except:
            return None

    
    def getByOrderIdAndProductId(self, id_pedido, id_produto):
        banco=DB()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT pedidos_id, produtos_id, quantidade, valor, observacao FROM pedidos_produtos WHERE pedidos_id = %s AND WHERE produtos_id = %s' , (id_pedido, id_produto))
            result = c.fetchall()
            c.close()
            return result
        except:
            return None


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
            c.execute('UPDATE pedidos SET pedidos_id = %s , produtos_id = %s , quantidade = %s, valor = %s, observacao = %s WHERE id = %s' , (self.pedidos_id , self.produtos_id , self.quatidade, self.valor, self.observacao, self.id))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do produto do pedido'


    def delete(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM pedidos_produtos WHERE id = %s' , (self.id))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do produto do pedido'