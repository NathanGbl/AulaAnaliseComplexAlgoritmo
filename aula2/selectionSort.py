def troca(V, i, menor):
    temp = V[i]
    V[i] = V[menor]
    V[menor] = temp

def selectionSort(V, n):
    for i in range(0, n - 1):
        menor = i
        for j in range(i+1, n):
            if V[j] < V[menor]:
                menor = j
        troca(V, i, menor)

vetor = [6, 5, 4, 3, 2, 1]

selectionSort(vetor, len(vetor))