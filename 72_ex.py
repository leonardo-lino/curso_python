

#macaco eu tentou abaixo e não conseguiu
# valor=1
# n_vezes = 5
# def multiplicar(valor,n_vezes):
#     i=0
#     while i <n_vezes:
#         valor *= (int(input("Digite um valor: ")))
#         i+=1
#         return valor 
    
# multiplicar()
# print(valor)



#codigo da aula
def multiplicar(*args): #args para receber quantos argumentos quiser
    total = 1
    for numero in args:
        total *= numero
    return total


def par_impar(n):
    if n % 2 ==0:
        return print(f'{n} é par.')
    else:
        return print(f'{n} é impar')



print(multiplicar(5,10))
par_impar(50)