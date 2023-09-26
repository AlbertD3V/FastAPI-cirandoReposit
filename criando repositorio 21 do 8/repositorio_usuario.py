import sqlite3
from dtos import UsuarioOut
class RepositorioUsuario:

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

   
    def consulta_um(self,nome_usuario):
        self.connect()
        self.cursor.execute("SELECT nome_usuario, nome_completo, cargo  FROM usuario WHERE nome_usuario = ?;",(nome_usuario,))
        um = self.cursor.fetchone()
        self.desconect()
        return self.criar_objeto(um)
        
    def criar_objeto(self, nome):
        nome_usuario, nome_completo, cargo = nome
        return UsuarioOut(nome_usuario=nome_usuario,  nome_completo=nome_completo, cargo=cargo)
   
    def inserir_usario(self,nome_usuario,nome_completo,cargo,salt_senha,hash_senha):
        self.connect()
        query = "INSERT OR IGNORE INTO usuario (nome_usuario,nome_completo,cargo,salt_senha,hash_senha) VALUES (?, ?, ?, ?, ?);"
        self.cursor.execute(query, (nome_usuario, nome_completo, cargo,salt_senha,hash_senha))
        self.conexao.commit()
        self.desconect()

    
    def consulta_salt(self,nome_usuario):
        self.connect()
        self.cursor.execute("SELECT salt_senha FROM usuario WHERE nome_usuario = ?;",(nome_usuario,))
        um = self.cursor.fetchone()
        self.desconect()
        return um

    def faz_login(self,nome_usuario,salt_senha,hash_senha):
        self.connect()
        self.cursor.execute("SELECT nome_usuario, nome_completo, cargo  FROM usuario WHERE nome_usuario = ? AND salt_senha = ? AND hash_senha = ?;",(nome_usuario,salt_senha,hash_senha))
        um = self.cursor.fetchone()
        self.desconect()
        return self.criar_objeto(um)