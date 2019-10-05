from models.DB import DB

class User():

    def __init__(self, nome='', login='', senha='', grupo=''):
        self.id = None
        self.nome = nome
        self.login = login
        self.senha = senha
        self.grupo = grupo


    def getAll(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT * FROM usuarios')
            result = c.fetchall()
            c.close()
            return result
        except:
            return None


    def get(self, id_usuario):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT id, nome, login, senha, grupo FROM usuarios WHERE id = %s' , (id_usuario))
            for linha in c:
                self.id=linha[0]
                self.nome=linha[1]
                self.login=linha[2]
                self.senha=linha[3]
                self.grupo=linha[4]
            c.close()
            if not self.id:
                return 'Usuário não encontrado!'
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do usuário'


    def insert(self):
        banco = DB()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO usuarios(nome, login, senha, grupo) VALUES (%s, %s, %s, %s)' , (self.nome, self.login, self.senha, self.grupo ))
            banco.conexao.commit()
            c.close()
            return 'Usuário cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do usuário'


    def update(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE usuarios SET nome = %s , login = %s , senha = %s, grupo = %s WHERE id = %s' , (self.nome , self.login , self.senha, self.grupo, self.id))
            banco.conexao.commit()
            c.close()
            return 'Usuário atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do usuário'


    def delete(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM usuarios WHERE id = %s' , (self.id))
            banco.conexao.commit()
            c.close()
            return 'Usuário excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do usuário'