#o argumento passado no split é onde irá quebrar a frase
#ex
frase = 'olha só, que coisa interessante'

lista_de_palavras = frase.split() #argumento vazio considera a quebra de #palavras no espaço em branco
print('Lista separada por espaço\n', lista_de_palavras)

lista_sep_virgula = frase.split(',')
print('Lista separada por virgula\n', lista_sep_virgula)

#join
#aula 93