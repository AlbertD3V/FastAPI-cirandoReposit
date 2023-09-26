import sqlite3
from dtos import ProdutoOut
from typing import List

class RepositorioProduto:

    def montar(self, tupla_dados: tuple) -> ProdutoOut:
        codigo, codigo_cardapio, nome, descricao, preco, restricao = tupla_dados
        preco = float(preco)
        return ProdutoOut(codigo=codigo, codigo_cardapio=codigo_cardapio, 
            nome=nome, descricao=descricao, preco=preco, restricao=restricao)

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

    def ler_produtos(self, preco_min: int = -1, preco_max: int = 99999, 
            codigo_cardapio: str = '', restricao: str = '') -> List[ProdutoOut]:
        
        query = 'SELECT codigo,codigo_cardapio,nome,descricao,preco,restricao FROM produto WHERE preco >= ? AND preco <= ?'

        parametros = [preco_min, preco_max]

        if codigo_cardapio:
            query += ' AND codigo_cardapio = ?'
            parametros.append(codigo_cardapio)

        if restricao:
            query += ' AND restricao = ?'
            parametros.append(restricao)

        query += ';'
        
        self.abrir_conexao()
        self.cursor.execute(query, tuple(parametros))
        produtos = self.cursor.fetchall()
        self.fechar_conexao()
        return [self.montar(produto) for produto in produtos]

    def consulta_um_produto(self,codigo):
        self.connect()
        self.codigo = codigo
        self.cursor.execute("SELECT * FROM produto WHERE codigo = ?;",(codigo,))
        um = self.cursor.fetchone()
        self.desconect()
        return self.montar(um)
        
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



    
