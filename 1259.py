N = int(input())

pares = []
impares = []

for i in range(N):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares = sorted(pares)
impares = sorted(impares, reverse = True)

for i in pares:
    print(i)

for i in impares:
    print(i)