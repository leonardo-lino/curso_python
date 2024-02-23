# Listas em Python
# Tipo list  - mutavel
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizaveis - indices e fatiamento
# Metódos úteis: append, insert, pop, del, clear, extend etc
#   append - adiciona um item ao final da lista
#   insert - adiciona um item no indice escolhido
#   pop - remove do final ou do indice escolhido
#   del - apaga uum indice
#   clear - limpa a lista
#   extend - estende a lista
#   + - -> concatena listas
#Create read update   delete
#Criar  Ler  Alterar apagar = lista[i] (CRUD)

lista = [10,20,30,40]

#AULA 1 DAQUI ATÉ A LINHA 28
# lista.append(50) # adiciona ao final da lista
# print('lista inteira:\n',lista, sep='')
# ultimo_valor =lista.pop() #remove o ultimo item da lista
# print('Ultimo item removido:\n', lista, sep='')
# #ao remover o ultimo item, retorna um valor inteiro no pop
# print('valor removido: ', ultimo_valor)
# print('lista restante:\n', lista, sep='')
# #removendo em um indice especifico
# lista.pop(2)#vai remover o indice 2
# print('lista com indice 2 removido:\n', lista, sep='')
# #FINAL DA AULA 1


#AULA 2
#delete
# lista.append('leonardo')
# print(lista) #lista adicionada o valor 'leonardo'
# nome = lista.pop()
# print(lista) #lista sem o 'leonardo'
# #DELETANDO O ULTIMO ITEM DA LISTA SEM SABER O INDICE
# #só usar o valor invertido
# del lista[-1]
# print(lista)
# lista.clear()
# print('Lista limpa: ', lista)
# #adicionando valor com insert
# lista.insert(0,10) #inseriu o valor 10 no indice 0
# lista.insert(1,20)
# print('Lista com os valores 10 e 20 adicionados:\n', lista, sep='')
#FINAL DA AULA 2


#AULA 3
#EXTEND E CONCATENAÇÃO DE LISTA
lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
print(f'Lista concatenada: \n{lista_c}')

#o extend não retorna nada, ele faz uma alteração diretamente na lista
#ou seja, não adianta mandar imprimir algo com o extend pq vai retornar
#'none', ja q não retorna nada. Tem que chamar a variavel que fez a #alteração com o extend
lista_extend_errada = lista_a.extend(lista_b)
print(f'Não irá retornar nada nesse print:\n',lista_extend_errada, sep='')
lista_a.extend(lista_b)#fez a alteração direto na lista a
print('Lista com o uso do extend corretamente:\n', lista_a, sep='')







