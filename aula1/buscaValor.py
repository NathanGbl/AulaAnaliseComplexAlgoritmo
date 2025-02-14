def buscaValor(v, k):
    for i in range(0, len(v)):
        if v[i] == k:
            return True
    return False

print(buscaValor([1,2,3,4,5], -2))