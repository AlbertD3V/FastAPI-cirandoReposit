from repositorio_cardapio import RepositorioCardapio


teste = RepositorioCardapio('db.sqlite')

#todos = teste.ler_todos()

#print(todos)

#um = teste.consulta_um('fastfood')

#print(um)

teste.inserir_cardapio("refri","Coca-Cola","todos")

coca = teste.consulta_um('refri')

print(coca)