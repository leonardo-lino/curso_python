'''Fatiamento de Strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
obs, a função len retorna a qnt de caracteres da string'''


var = 'Olá mundo'
#ex de fatiamento
print(var[4:]) #do indice 4 até #o final

#ex de fatiamento com o passo (p)
print(var[0:9:2]) #vai pular de 2 em 2

#da para colocar valor negativo para fazer a leitura invertida
print(var[::-1])