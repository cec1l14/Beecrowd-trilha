q_par = q_impar = q_pos = q_neg = 0

for i in range(5):
    num = int(input())
    if num > 0:
        q_pos += 1
    elif num < 0:
        q_neg += 1
    if num%2 == 0:
        q_par += 1
    else:
        q_impar += 1

print(f"{q_par} valor(es) par(es)")
print(f"{q_impar} valor(es) impar(es)")
print(f"{q_pos} valor(es) positivo(s)")
print(f"{q_neg} valor(es) negativo(s)")
