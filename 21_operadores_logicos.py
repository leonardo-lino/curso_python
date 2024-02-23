#foi citado antes os basicos q ja sei

# operador not serve para inverter
#ex: not True vira False e not #False vira True

  

#operadores in e not in
#Strings são iteraveis
#0 1 2 
#L e o 
#-3-2-1
# nome = 'Leo'
# print(nome[0]) 
# print('eo' in nome) #retoarna True
# print('nson' in nome) #retorna false


#EXERCICIO

nome = input("Digite seu nome: ")
encontrar = input("Digite o que quer encontrar: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')