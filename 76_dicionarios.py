





pessoa = {
    'nome': 'Leonardo',
    'sobrenome': 'Lino',
    'idade': 28,
    'altura': 171,
    'endereços':[
        {'rua': 'almirante tamandaré', 'numero': 371},
        {'rua': 'dos pintassilgos', 'numero': 202, 'complemento':'202c'},
    ]
}

#print(pessoa['nome'] + ' ' + pessoa['sobrenome'])

print('Pessoa sem cpf:')
for chave in pessoa:
    print(chave, pessoa[chave])


#para criar novas chaves é só criar como se fosse variavel. Ex:
pessoa['cpf'] = '06629073533'
print('Pessoa com cpf:')
for chave in pessoa:
    print(chave, pessoa[chave])