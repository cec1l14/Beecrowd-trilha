valor_produto = float(input("Informe o valor do produto: "))
forma_pagamento = input("Informe a forma de pagamento (Dinheiro/Cheque): ")

if valor_produto >= 100.0 and forma_pagamento == "Dinheiro":
    valor_produto = valor_produto - (0.1 * valor_produto)
    print(f"R$ {valor_produto:.2f}")
elif forma_pagamento == "Cartão":
    print("Forma de pagamento inválida")
else:
    print(f"R$ {valor_produto:.2f}")
