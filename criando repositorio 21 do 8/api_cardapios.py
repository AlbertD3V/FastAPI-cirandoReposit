from fastapi import APIRouter, HTTPException, status, Depends
import db
import dtos
from util import Utilidades
from repositorio_cardapio import RepositorioCardapio
from repositorio_produto import RepositorioProduto
from dependencia import obter_rep_cardapio,obter_rep_produto

router = APIRouter()

@router.get('/cardapio/')
async def listar_cardapios(repo_cardapio: RepositorioCardapio = Depends(obter_rep_cardapio)):
 
    return repo_cardapio.ler_todos
 
@router.get('/cardapio/{codigo_cardapio}')
async def consultar_cardapio(codigo_cardapio: str,repo_cardapio: RepositorioCardapio = Depends(obter_rep_cardapio)):
    consulta = repo_cardapio.consulta_um(codigo_cardapio)
    if not consulta:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
            'Cardápio não encontrado.')
 
    return consulta
 
@router.post('/cardapio/', status_code=status.HTTP_201_CREATED)
async def cadastrar_cardapio(cardapio: dtos.CardapioIn,
    util: Utilidades = Depends(Utilidades),repo_cardapio: RepositorioCardapio = Depends(obter_rep_cardapio)):
 
    codigo = util.criar_codigo(cardapio.nome)
 
    if repo_cardapio.consulta_um(codigo):
        raise HTTPException(status.HTTP_400_BAD_REQUEST,
            'Código já existe.')
 
    repo_cardapio.inserir_cardapio(codigo, cardapio.nome, cardapio.descricao)
    return repo_cardapio.consulta_um(codigo)
 
@router.put('/cardapio/{codigo_cardapio}')
async def alterar_cardapio(codigo_cardapio: str, cardapio: dtos.CardapioIn,repo_cardapio: RepositorioCardapio = Depends(obter_rep_cardapio)):
 
    if repo_cardapio.consulta_um(codigo_cardapio):
        raise HTTPException(status.HTTP_404_NOT_FOUND,
            'Cardápio não encontrado.')
 
    repo_cardapio.alterar(codigo_cardapio,cardapio.nome,cardapio.descricao)
    return repo_cardapio.consulta_um(codigo_cardapio)
 
@router.delete('/cardapio/{codigo_cardapio}')
async def remover_cardapio(codigo_cardapio: str,repo_cardapio: RepositorioCardapio = Depends(obter_rep_cardapio),repor_produto:RepositorioProduto = Depends(obter_rep_produto)):
 
    if repo_cardapio.consulta_um(codigo_cardapio):
        raise HTTPException(status.HTTP_404_NOT_FOUND,
            'Cardápio não encontrado.')
    
    if repor_produto.consulta_um(codigo_cardapio):
         raise HTTPException(status.HTTP_400_BAD_REQUEST,
            'Não é possível deletar. Cardápio possui produtos.')
 
    return repo_cardapio.delete(codigo_cardapio)
 
@router.patch('/cardapio/{codigo_cardapio}')
async def alterar_descricao_cardapio(codigo_cardapio: str, 
    descricao: dtos.DescricaoCardapio,repo_cardapio: RepositorioCardapio = Depends(obter_rep_cardapio)):
    
    if repo_cardapio.consulta_um(codigo_cardapio):
        raise HTTPException(status.HTTP_404_NOT_FOUND,
            'Cardápio não encontrado.')
 
    db.banco_cardapios[codigo_cardapio]['descricao'] = descricao.descricao
    return 
