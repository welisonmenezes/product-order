from models.DB import DB

class Order():

    def __init__(self, data_hora='', observacao='', clientes_id=None):
        self.id = None
        self.data_hora = data_hora
        self.observacao = observacao
        self.clientes_id = clientes_id


    def getAll(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT * FROM pedidos')
            result = c.fetchall()
            c.close()
            return result
        except:
            return None


    def get(self, id_pedido):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT id, data_hora, observacao, clientes_id FROM pedidos WHERE id = %s' , (id_pedido))
            for linha in c:
                self.id=linha[0]
                self.data_hora=linha[1]
                self.observacao=linha[2]
                self.clientes_id=linha[3]
            c.close()
            if not self.id:
                return 'Pedido não encontrado!'
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do pedido'


    def insert(self):
        banco = DB()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO pedidos(data_hora, observacao, clientes_id) VALUES (%s, %s, %s)' , (self.data_hora, self.observacao, self.clientes_id))
            banco.conexao.commit()
            self.id = c.lastrowid
            c.close()
            return 'Pedido cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do pedido'


    def update(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE pedidos SET data_hora = %s , observacao = %s , clientes_id = %s WHERE id = %s' , (self.data_hora , self.observacao , self.clientes_id, self.id))
            banco.conexao.commit()
            c.close()
            return 'Pedido atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do pedido'


    def delete(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM pedidos WHERE id = %s' , (self.id))
            banco.conexao.commit()
            c.close()
            return 'Pedido excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do pedido'