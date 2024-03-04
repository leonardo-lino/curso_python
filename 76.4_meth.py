p1 = {
    'nome': 'Leonardo',
    'sobrenome': 'Lino',
}

print(p1.get('nome'))

ultima_chave = p1.popitem()
print(f'Chave apagada: {ultima_chave}')
print(f'Chave atualizada com chave apagada: {p1}')

#UPDATE
# p1.update({
#     'sobrenome': 'Oliveira',
#     'idade': 28
# })

#ou 

p1.update(nome='Novo nome', idade=30)
print(p1)