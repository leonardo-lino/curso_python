nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
espaco = ' '

if nome != '' and idade != '':
    #imprime nome
    print(f'Seu nome é {nome}')
    
    #imprime nome invertido
    print(f'Seu nome invertido é {nome[::-1]}')

    #imprime se tem espaço
    if espaco in nome:
        print('Seu nome tem espaço.')
    else:
        print('Seu nome não tem espaço. ')
    
    #imprime qnt de letras
        
        print(f'seu nome tem {len(nome)} letras')

    #imprime a primeira letra
        print(f'A primeira letra de seu nome é: {nome[0]}')

    #imprime a ultima letra
        print(f'A ultima letra de seu nome é {nome[len(nome)-1]}')
else:
    print('Desculpe, você deixou campos vazios')
