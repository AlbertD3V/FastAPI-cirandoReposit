from dotenv import dotenv_values
from repositorio_cardapio import RepositorioCardapio
from repositorio_produto import RepositorioProduto
from repositorio_usuario import RepositorioUsuario
from autenticacao import Autenticador
from fastapi.security import OAuth2PasswordBearer


ENV = dotenv_values() 

def obter_rep_cardapio():
    return RepositorioCardapio(ENV["BANCO_DADOS"])

def obter_rep_produto():
    return RepositorioProduto(ENV["BANCO_DADOS"])

def obter_rep_usuario():
    return RepositorioUsuario(ENV["BANCO_DADOS"])

def obter_autenticador():
    return Autenticador(ENV['ALGORITMO'], ENV['CHAVE_PRIVADA'], ENV['CHAVE_PUBLICA'], int(ENV['VALIDADE_TOKEN']),int(ENV['CUSTO_SALT']))

dependencia_token = OAuth2PasswordBearer(tokenUrl=ENV['URL_TOEKN'])
