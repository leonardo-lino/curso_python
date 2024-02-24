cpf = '06629073533'

nove_digitos = cpf[:9] #fatiamento que vai do 0 ao 9

contador_regresivo = 10

soma = 0
for digito in nove_digitos:
    print(digito, contador_regresivo)
    multi = int(digito) * contador_regresivo
    soma += multi
    contador_regresivo -=1
print(soma)

multip_por_10 = (soma*10) % 11

print(multip_por_10)