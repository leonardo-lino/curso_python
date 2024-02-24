#tupla é como uma lista, mas IMUTÁVEL
#para criar uma tubla, é só não colocar a "lista" em colchetes, exemplo:
nomes_lista = ['Maria', 'Helena', 'Leonardo']
nomes_tupla = 'Maria', 'Helena', 'Leonardo' #isso é uma tupla

#para transformar uma lista em uma tupla:
nomes_tupla_nova = tuple(nomes_lista)
# e para transformar uma tupla em uma lista, serve a mesma logica
nomes_lista_nova =list(nomes_tupla)
print(nomes_lista_nova)