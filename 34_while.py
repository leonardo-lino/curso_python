nome = 'Leonardo'

indice = 0

# while indice < len(nome):
#     print(nome[indice])
#     print('*')
#     indice+=1

novonome = ''

while indice < len(nome):
    letra = nome[indice]
    novonome += '*'
    novonome +=letra
    indice+=1
novonome += '*'
print(novonome)