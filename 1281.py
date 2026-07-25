N = int(input())

for i in range(N):
    M = int(input())
    prod = {}
    valor = 0

    for j in range(M):
        p, pr = input().split()
        prod[p] = float(pr)

    P = int(input())

    for k in range(P):
        cp, v = input().split()

        if cp in prod:
            valor += float(v)*prod[cp]


    print(f"R$ {valor:.2f}")