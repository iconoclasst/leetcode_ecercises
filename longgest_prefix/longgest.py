
#longgest prefix string
# Encontrar o prefixo comum mais longo entre todas as strings de um array de strings

str = ["flower","flow","flight"]

prefix = max(str)

for i in range(len(str)):
    comp = str[i]
    for j in range(len(comp) -1, -1, -1):
        if comp[j] != comp[j - 1]:
            prefix[-1] = ''
        else:
            break

print(max(str))
