from models.DB import DB

class Client():

    def __init__(self, nome='', endereco='', numero='', observacao='', cep='', bairro='', cidade='', estado='', telefone='', email='', login='', senha='', grupo=''):
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
        self.login = login
        self.senha = senha
        self.grupo = grupo


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
            c.execute('SELECT * FROM clientes WHERE id = %s' , (id_cliente))
            for linha in c:
                self.id=linha[0]
                self.login=linha[1]
                self.senha=linha[2]
                self.grupo=linha[3]
                self.nome=linha[4]
                self.endereco=linha[5]
                self.numero=linha[6]
                self.observacao=linha[7]
                self.cep=linha[8]
                self.bairro=linha[9]
                self.cidade=linha[10]
                self.estado=linha[11]
                self.telefone=linha[12]
                self.email=linha[13]
            c.close()
            if not self.id:
                return 'Cliente não encontrado!'
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do cliente'

    def getByLogin(self, login):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT * FROM clientes WHERE login = %s' , (login))
            for linha in c:
                self.id=linha[0]
                self.login=linha[1]
                self.senha=linha[2]
                self.grupo=linha[3]
                self.nome=linha[4]
                self.endereco=linha[5]
                self.numero=linha[6]
                self.observacao=linha[7]
                self.cep=linha[8]
                self.bairro=linha[9]
                self.cidade=linha[10]
                self.estado=linha[11]
                self.telefone=linha[12]
                self.email=linha[12]
            c.close()
            if not self.id:
                return 'Usuário não encontrado!'
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do usuário'


    def insert(self):
        banco = DB()
        #try:
        c = banco.conexao.cursor()
        c.execute('INSERT INTO clientes(login, senha, grupo, nome, endereco, numero, observacao, cep, bairro, cidade, estado, telefone, email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)' , (self.login, self.senha, self.grupo, self.nome, self.endereco, self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email ))
        banco.conexao.commit()
        self.id = c.lastrowid
        c.close()
        return 'Cliente cadastrado com sucesso!'
        # except:
        #     return 'Ocorreu um erro na inserção do cliente'


    def update(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE clientes SET login = %s, senha = %s, grupo = %s, nome = %s , endereco = %s , numero = %s, observacao = %s, cep = %s, bairro = %s, cidade = %s, estado = %s, telefone = %s, email = %s WHERE id = %s' , (self.login, self.senha, self.grupo, self.nome , self.endereco , self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email, self.id))
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