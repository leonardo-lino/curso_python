'''
quando usamos o sinal de igualdade para atribuir um valor à um item mutavel, temos que lembrar sempre que o sinal ed igualdade não cria uma cópia, mas faz o ponteiro sinalizar para o mesmo lugar da memoria. então para fazer uma copia, se usa o metodo copy(). 
Exemplo:
'''
#ao igualar d1 com d2, eu to atribuindo às duas variaveis o mesmo local na memoria
d1 = {
    'c1': 1,
    'c2': 2
}

d2 = d1 #aqui eu atribui o mesmo local na memoria. Não é uma copia, é um endereçamento identico

d2['c1'] = 100
print(f'd1: {d1}') #aqui podemos ver que o d1 foi alterado, mesmo nós temos atualizado "apenas o d2". Isso ocorre pq o d2 aponta para o mesmo lugar do d1. Então está alterando o mesmo endereço das duas variaveis
 

#Para fazer da forma correta, se usa o .copy()

d3 = {
    'c1': 1,
    'c2': 2
}
d4 = d3.copy()
d4['c1'] = 1500
print(f'd3: {d3}')
print(f'd4: {d4}')
#percebe-se acima que foi mudado o valor em d4 mas não em d3.
#Mas mesmo assim, isso é uma shallow copy (copia casa), pq funciona apenas para valores imutaveis. Para valores mutaveis, como listas, ele não faz copia, faz o endereçamento para o mesmo local

#Para fazer uma copia profunda (deep copy), se importa uma biblioteca chamada copy, e ai se faz com o comando deepcopy(). Ex:
import copy
d5 = copy.deepcopy(d4)
d5['c1'] = 999
print(f'd5: {d5}')