import sqlite3

class RepositorioProduto:

    def __init__(self, db):
        self.nome = db
        self.conexao = None
        self.cursor = None

    def connect(self):
        self.conexao = sqlite3.connect("db.sqlite")
        self.cursor = self.conexao.cursor()

    def desconect(self):
        self.cursor = self.cursor.close()
        self.conexao = self.conexao.close()
        self.cursor = None
        self.conexao = None

    def inserir_produto(self,codigo,codigo_cardapio,nome,descricao,preco:float,restricao):
        self.connect()
        query = "INSERT OR IGNORE INTO produto (codigo,codigo_cardapio, nome, descricao,preco,restricao) VALUES (?, ?, ?, ?, ?, ?);"
        self.cursor.execute(query, (codigo,codigo_cardapio, nome, descricao,preco,restricao))
        self.conexao.commit()
        self.desconect()

    def ler_produtos(self):
        self.connect()
        self.cursor.execute("SELECT * FROM produto")
        todos = self.cursor.fetchall()
        self.desconect()
        return todos

    def consulta_um_produto(self,codigo):
        self.connect()
        self.codigo = codigo
        self.cursor.execute("SELECT * FROM produto WHERE codigo = ?;",(codigo,))
        um = self.cursor.fetchone()
        self.desconect()
        return um
        
    def alterar_produto(self,codigo,codigo_cardapio,nome,descricao,preco:float,restricao):
        self.connect()
        query = "UPDATE produto SET nome = ?, descricao = ?, preco = ?, codigo_cardapio = ?, restricao = ? WHERE codigo = ?;"
        self.cursor.execute(query, (nome,descricao,preco,codigo_cardapio,restricao,codigo))
        self.conexao.commit()
        self.desconect()

    def delete_produto(self,codigo):
        self.connect()
        self.codigo = codigo
        self.cursor.execute("DELETE FROM produto WHERE codigo = ?;", (codigo,))
        self.conexao.commit()
        self.desconect()



    
