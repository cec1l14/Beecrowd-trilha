N = int(input())

for i in range(N):
    quant = 0

    X = int(input())

    for j in range(1, X + 1):
        if X % j == 0:
            quant += 1

    if quant == 2:
        print(f"{X} eh primo")

    else:
        print(f"{X} nao eh primo")