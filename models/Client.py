from models.DB import DB

class Client():

    def __init__(self, nome='', endereco='', numero='', observacao='', cep='', bairro='', cidade='', estado='', telefone='', email=''):
        self.id = None
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.observacao =observacao
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.email = email


    def getAll(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT * FROM clientes')
            result = c.fetchall()
            c.close()
            return result
        except:
            return None


    def get(self, id_cliente):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT id, nome, endereco, numero, observacao, cep, bairro, cidade, estado, telefone, email FROM clientes WHERE id = %s' , (id_cliente))
            for linha in c:
                self.id=linha[0]
                self.nome=linha[1]
                self.endereco=linha[2]
                self.numero=linha[3]
                self.observacao=linha[4]
                self.cep=linha[5]
                self.bairro=linha[6]
                self.cidade=linha[7]
                self.estado=linha[8]
                self.telefone=linha[9]
                self.email=linha[10]
            c.close()
            if not self.id:
                return 'Cliente não encontrado!'
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do cliente'


    def insert(self):
        banco = DB()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO usuarios(nome, endereco, numero, observacao, cep, bairro, cidade, estado, telefone, email) VALUES (%s, %s, %s, %s)' , (self.nome, self.endereco, self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email ))
            banco.conexao.commit()
            c.close()
            return 'Cliente cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do cliente'


    def update(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE usuarios SET nome = %s , endereco = %s , numero = %s, observacao = %s, cep = %s, bairro = %s, cidade = %s, estado = %s, telefone = %s, email = %s WHERE id = %s' , (self.nome , self.endereco , self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email, self.id))
            banco.conexao.commit()
            c.close()
            return 'Cliente atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do cliente'


    def delete(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM clientes WHERE id = %s' , (self.id))
            banco.conexao.commit()
            c.close()
            return 'Cliente excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do cliente'