'''
 len =  quantas chaves
 keys = iteravel com as chaves
 values - iteravel com os valores
 items - iteravel com chaves e valores
 setdefault - adiciona valor se a chave nãoe xiste
 copy - retorna uma copia rasa (shallow copy)
 get - obtem uma chave
 pop - apaga um item com chave especificada (del)
 pop item - apaga o ultimo item adicionado
 update - atualiza um dicionario com outro
'''

pessoa = {
    'nome': 'Leonardo',
    'sobrenome': 'Oliveira',
    'sobrenome':'Lino' #obs: se adicionar chaves iguais, o ultimo valor será atribuido
}
#abaixo retorna as keys do dicionario
#print(list(pessoa.keys()))
#abaixo retorna os valuyes do dicionario
#print(list(pessoa.values()))

#setdefault adiciona um default
pessoa.setdefault('idade','0')

#"items" retorna a chave e o valor
for chave, valor in pessoa.items():
    print(chave, valor)