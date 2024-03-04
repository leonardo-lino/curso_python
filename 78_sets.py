
# Sets - Conjuntos em Python
# Conjuntos são ensinados na matematica (são os mesmos da escola)
# São representados graficamente pelo diagrama de Venn.
# Sets em python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set:
# set(iteravel) ou {1,2,3}
s1 = set() #set vazio
s1 = {'Leonardo',1,2,3,True} #com dados


# Sets são eficientes para remover valores duplicados de iteráveis.
#     - eles ñao tem indexes
#     - eles não garantem ordem
#     - eles são iteraveis (for, in, not in)

s2 = {1,1,1,1,1,1,2,2,2,3,3,3,}
print(s2)
# Metodos úteis:
# add,update, clear, discard

# PARECEM dicionários mas não são. Os sets não tem par de chaves/valor, tem apenas valor.

