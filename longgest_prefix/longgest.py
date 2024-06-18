
#longgest prefix string
# Encontrar o prefixo comum mais longo entre todas as strings de um array de strings


def lcp(str):
    words = sorted(str)

    w1 = words[0]
    w2 = words[-1]

    resp = ""

    for i in range(len(min(w1, w2))):
        if w1[i] == w2[i]:
            resp += w1[i]
        else:
            break
    return resp

str = ["flower","flow","flight"]
print(lcp(str))







        

        
        
    

# print(resp)