while True:

    lista = []
    soma = 0

    M, N = map(int, input().split())
    
    if M <= 0 or N <= 0:
        break
    
    elif M > N:
        M, N = N, M

    for i in range(M, N + 1):
        lista.append(i)
        soma += i
    
    print(*lista, "Sum=" + str(soma))


