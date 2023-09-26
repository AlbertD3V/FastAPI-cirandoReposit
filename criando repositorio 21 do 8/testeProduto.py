from repositorio_produto import RepositorioProduto


teste = RepositorioProduto('db.sqlite')

#todos = teste.ler_produtos()

#print(todos)

#um = teste.consulta_um_produto('x-burguer')

#print(um)

#teste.inserir_produto("Coca-Cola","fastfood","Coca Cola","suco preto gaseficado",7.9,"padrao")

#coca = teste.consulta_um_produto("Coca-Cola")

#print(coca)

trocar = teste.alterar_produto("Coca-Cola","refri","Coca Cola","O melhor suco preto gaseficado",7.5,"todos")
um = teste.consulta_um_produto("Coca-Cola")

print(um)