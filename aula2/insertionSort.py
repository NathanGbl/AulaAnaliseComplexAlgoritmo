import time
def InsertionSort(V, n):
    for i in range(1, n):
        chave = V[i]
        j = i - 1
        while j>= 0 and V[j] > chave:
            V[j+1] = V[j]
            j = j - 1
            V[j+1] = chave

vetor = [6, 5, 4, 3, 2, 1]

print(vetor)
inicio = time.process_time()
InsertionSort(vetor, len(vetor))
fim = time.process_time()
intervalo = fim - inicio
print(intervalo)
print(vetor)