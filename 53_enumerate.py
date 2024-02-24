lista = ['Maria', 'Helena', 'Leonardo']
lista.append('João')

# #AULA PARTE 1
# lista_eumerada = enumerate(lista)
# #print(lista_eumerada) #vai imprimir uns codigo feio
# #para imprimir uma lista enumerade, pode-se usar o for:
# for item in lista_eumerada:
#     print(item)
# #FINAL DA AULA PARTE 1


#AULA PARTE 2
#pegando indices com o enumerate

for indice, nome in enumerate(lista):
    print(indice, nome)