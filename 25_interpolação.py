# Interpolação básica de Strings
# s - string 
# d e i - int 
# f - float 
# x e X - Hexadecimal(ABCDEF0123456789)


# nome = 'Leonardo'
# preco = 1000.9182791287
# var = '%s, o preco é R$%.2f' %(nome, preco)
# print(var)


#FORMATAÇÃO BÁSICA DE STRINGS

# .<numero de digitos>f 
# > - esquerda
# < - direita
# ^ - centro
# (caractere)(<>^)(quantidade)

# ex: 0>-100,.1f
# ex2: 
variavel = 'abc'
print(f'{variavel}')
print(f'{variavel:.>10}')
print(f'{variavel:.<10}')
print(f'{variavel:.^10}')