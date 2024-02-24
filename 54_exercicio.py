import os
lista = []

while True: 
    op = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar')
    if op not in 'ial':
        print('Digite uma opção válida.')
    else:
        match op:
############ - INSERINDO ITENS - #########################################
            case 'i':
                lista.append(input('Digite o item a ser inserido: '))
                os.system('cls')
            
############ - APAGANDO ITEM - ###########################################
            case 'a':
                for indice, item in enumerate(lista):
                    print(indice, item)
                
                try:
                    item_para_excluir = int(input('Digite um indice para excluir: '))
                    if item_para_excluir < len(lista):
                        lista.pop(item_para_excluir)
                        os.system('cls')
                    else:
                        print(f'Digite um indice válido.')
                except ValueError:
                    print('Digite apenas números')
                except Exception:
                    print('Erro desconhecido.')

############-LISTANDO OS ITENS###########################################
            case 'l':
                if len(lista) == 0:
                    print('Nada para listar.')
                else:
                    print('LISTA DE ITENS: ')
                    for indice, item in enumerate(lista):
                        print(indice, item)
