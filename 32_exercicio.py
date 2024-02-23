
#exercicio 1
# n = int(input('Digite um número: '))

# if n % 2 == 0:
#     print(f'{n} é par.')
# else:
#     print(f'{n} é impar')


#exercicio 2
try:
    hora = int(input('Que horas são? '))

    if hora >=0 and hora <=11:
        print('Bom dia')

    elif hora >=12 and hora <=17:
        print('Boa tarde')
    elif hora >=18 and hora <=23:
        print('Boa noite')
    else:
        print('Valor digitado inválido.')
except:
    print('digite apenas número inteiros')

# #exercicio 3
# nome = input("Digite seu nome: ")

# if len(nome) <= 4:
#     print('Seu nome é curto')
# elif len(nome)>= 5 and len(nome)<=6:
#     print('seu nome é normal')
# elif len(nome) > 6:
#     print('seu nome é mt grande')