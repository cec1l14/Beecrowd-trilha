pares = []
impares = []

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
        if len(pares) == 5:
            for i in range(5):
                print(f"par[{i}] = {pares[i]}")
            pares = []
    else:
        impares.append(n)
        if len(impares) == 5:
            for i in range(5):
                print(f"impar[{i}] = {impares[i]}")
            impares = []
    
for i in range(len(impares)):
    print(f"impar[{i}] = {impares[i]}")

for i in range(len(pares)):
    print(f"par[{i}] = {pares[i]}")