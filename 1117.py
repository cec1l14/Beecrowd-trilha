quant = soma = 0

while quant != 2:

    nota = float(input())

    if nota < 0 or nota > 10:
        print("nota invalida")
    else:
        quant += 1
        soma += nota

media = soma/2
print(f"media = {media:.2f}")
