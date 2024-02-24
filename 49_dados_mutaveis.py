#cuidado com os dados mutáveis
#qnd aponta uma variavel para um valor imutavel, ela copia o valor
#quando aponta puma variavel apr aum valor mutavel, aponta o ponteiro para o mesmo valor na memoria


#noe xemplo abaixo, tá apenas apontando o ponteiro da lista b para o #mesmo local da memoria da lista a (não está copiando valores)
lista_a = ['Leonardo', 'José',1, 30,5, True]
lista_b = lista_a
print('Lista copiada:\n', lista_b, sep='')

lista_a[0] = 'Edmundo'
print(lista_a)

#Para copiar valores, se usa o comando copy; ai não vai apenas apontar o ponteiro para o mesmo endereço, vai copiar todos os valores da lista
lista_b = lista_a.copy
lista_a[0] = 'Lionardo'
print(lista_a)
print(lista_b)