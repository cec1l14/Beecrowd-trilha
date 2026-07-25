N = int(input())
for i in range(N):
    M = int(input())
    notas = list(map(int, input().split()))

    copia = notas[:]
    notas = sorted(notas, reverse = True)

    qtd = 0

    for i in range(M):
        if notas[i] == copia[i]:
            qtd += 1

    print(qtd)