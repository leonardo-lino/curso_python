perguntas = [
    {
    'Pergunta': 'Quanto é 1+1',
    'Opções': ['1','2','3','4'],
    'Resposta': '2'
    },
    {
    'Pergunta': 'Quanto é 5+5',
    'Opções': ['1','2','10','4'],
    'Resposta': '10'
    },
    {
    'Pergunta': 'Quanto é 3+3',
    'Opções': ['6','2','3','4'],
    'Resposta': '6'
    },
]

acertos = 0
erros = 0
for indice, pergunta in enumerate(perguntas):
    print('Pergunta: ' + pergunta.get('Pergunta'))
    resposta = input('Escolha uma opção:')
    
    if resposta == pergunta.get('Resposta'):
        print('Acertou!')
        acertos +=1
    else:
        print('Errou!')
        erros +=1
    
print(f'Você acertou {acertos} de {len(perguntas)} perguntas')