


# def mult_2(n):
#     return n*2

# def mult_3(n):
#     return n*3

# def mult_4(n):
#     return n*4


# print(mult_2(5))
# print(mult_3(5))
# print(mult_4(5))


#forma do prof:

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))