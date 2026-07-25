N = []

for i in range(20):
    N.append(int(input()))

V = N[:]

for i in range(10):
    N[i] = V[19 - i]

for i in range(10,20):
    N[i] = V[-1-i]

for i in range(20):
    print(f"N[{i}] = {N[i]}")