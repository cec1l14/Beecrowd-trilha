L = int(input())
T = input()
matriz = [[None]*12 for i in range(12)]

for i in range(12):
    for j in range(12):
            matriz[i][j] = float(input())

soma = 0

for i in range(12):
      soma += matriz[L][i]

media = soma/12

if T == "S":
      print(f"{soma:.1f}")
else:
      print(f"{media:.1f}")