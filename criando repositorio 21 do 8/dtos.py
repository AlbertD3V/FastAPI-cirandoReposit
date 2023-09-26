from pydantic import BaseModel, Field, validator, SecretStr
from util import Utilidades
from typing import Literal

class CardapioOut(BaseModel):
    codigo: str = Field(min_length=2, max_length=50)
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)

    @validator('codigo')
    def validar_codigo(codigo: str) -> str:
        return Utilidades.is_alnum_under(codigo)

class CardapioIn(BaseModel):
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)
 
class DescricaoCardapio(BaseModel):
    descricao: str = Field(max_length=255)
 
class ProdutoOut(BaseModel):
    codigo: str = Field(min_length=2, max_length=50)
    codigo_cardapio: str = Field(min_length=2, max_length=50)
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)
    preco: float = Field(gt=0)
    restricao: str = Field(min_length=2, max_length=20)

    @validator('codigo', 'codigo_cardapio')
    def validar_codigo(codigo: str) -> str:
        return Utilidades.is_alnum_under(codigo)

class ProdutoIn(BaseModel):
    codigo_cardapio: str = Field(min_length=2, max_length=50)
    nome: str = Field(min_length=2, max_length=50)
    descricao: str = Field(max_length=255)
    preco: float = Field(gt=0)
    restricao: str = Field(min_length=2, max_length=20)

    @validator('codigo_cardapio')
    def validar_codigo(codigo: str) -> str:
        return Utilidades.is_alnum_under(codigo)
 
class PrecoProduto(BaseModel):
    preco: float = Field(gt=0)

class UsuarioOut(BaseModel):
    nome_usuario: str = Field(min_length=6, max_length=20)
    nome_completo: str = Field(min_length=6, max_length=20)
    cargo: str = Field(min_length=2, max_length=20)

    

class Cadastro(BaseModel):
    nome_completo: str = Field(min_length=6, max_length=20)
    cargo: str = Field(min_length=2, max_length=20)
    senha: SecretStr = Field(min_length=6, max_length=20)

    @validator('nome_completo')
    def validar_nome_completo(texto: str) -> str:
        return Utilidades.is_alpha_space(texto)

    @validator('cargo')
    def validar_cargo(texto:str) -> str:
        pass

    @validator('senha')
    def validar_senha():
        pass


class BearerToken(BaseModel):
    access_token: str
    token_type: Literal['bearer'] = Field(default='bearer')
