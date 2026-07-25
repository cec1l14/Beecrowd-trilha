O = input()

matriz = [[None]*12 for i in range(12)]

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input())

soma = 0
inicio, fim = 1, 11

for i in range(5):
    for j in range(inicio, fim):
        soma += matriz[i][j]
    inicio += 1
    fim -= 1

media = soma/30

if O == "S":
    print(f"{soma:.1f}")
else:
    print(f"{media:.1f}")