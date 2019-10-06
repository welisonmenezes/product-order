from models.DB import DB

class Product():

    def __init__(self, descricao='', valor='', imagem=None):
        self.id = None
        self.descricao = descricao
        self.valor = valor
        self.imagem = imagem


    def getAll(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT * FROM produtos')
            result = c.fetchall()
            c.close()
            return result
        except:
            return None


    def get(self, id_produto):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT id, descricao, valor, imagem FROM produtos WHERE id = %s' , (id_produto))
            for linha in c:
                self.id=linha[0]
                self.descricao=linha[1]
                self.valor=linha[2]
                self.imagem=linha[3]
            c.close()
            if not self.id:
                return 'Produto não encontrado!'
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do produto'


    def insert(self):
        banco = DB()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO produtos(descricao, valor, imagem) VALUES (%s, %s, %s)' , (self.descricao, self.valor, self.imagem))
            banco.conexao.commit()
            c.close()
            return 'Produto cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do produto'


    def update(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE produtos SET descricao = %s , valor = %s , imagem = %s WHERE id = %s' , (self.descricao , self.valor , self.imagem, self.id))
            banco.conexao.commit()
            c.close()
            return 'Produto atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do produto'


    def delete(self):
        banco=DB()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM produtos WHERE id = %s' , (self.id))
            banco.conexao.commit()
            c.close()
            return 'Produto excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do produto'