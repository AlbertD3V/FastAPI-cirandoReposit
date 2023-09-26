import sqlite3
from dtos import CardapioOut

class RepositorioCardapio:

    def __init__(self, db):
        self.nome = db
        self.conexao = None
        self.cursor = None

    def criar_objeto(self, tupla):
        codigo, nome, descricao = tupla
        return CardapioOut(codigo=codigo,  nome=nome, descricao=descricao)

    def connect(self):
        self.conexao = sqlite3.connect("db.sqlite")
        self.cursor = self.conexao.cursor()

    def desconect(self):
        self.cursor = self.cursor.close()
        self.conexao = self.conexao.close()
        self.cursor = None
        self.conexao = None

    def inserir_cardapio(self,codigo,nome,descricao):
        self.connect()
        query = "INSERT OR IGNORE INTO cardapio (codigo, nome, descricao) VALUES (?, ?, ?);"
        self.cursor.execute(query, (codigo, nome, descricao))
        self.conexao.commit()
        self.desconect()

    def ler_todos(self):
        self.connect()
        self.cursor.execute("SELECT * FROM cardapio")
        todos = self.cursor.fetchall()
        self.desconect()
        return [self.criar_objeto(um) for um in todos]

    def consulta_um(self,codigo):
        self.connect()
        self.codigo = codigo
        self.cursor.execute("SELECT * FROM cardapio WHERE codigo = ?;",(codigo,))
        um = self.cursor.fetchone()
        self.desconect()
        return self.criar_objeto(um)
        
    def alterar(self,codigo,nome,descricao):
        self.connect()
        query = "UPDATE cardapio SET nome = ?, descricao = ? WHERE codigo = ?;"
        self.cursor.execute(query, (nome,descricao,codigo))
        self.conexao.commit()
        self.desconect()

    def delete(self,codigo):
        self.connect()
        self.codigo = codigo
        self.cursor.execute("DELETE FROM cardapio WHERE codigo = ?;", (codigo,))
        self.conexao.commit()
        self.desconect()



    
