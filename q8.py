valor_produto = float(input("Informe o valor do produto: "))
forma_pagamento = input("Informe a forma de pagamento (Dinheiro/Cheque/Cartão): ")

if valor_produto >= 100.0 and forma_pagamento == "Dinheiro":
    valor_produto = valor_produto - (0.1 * valor_produto)
    print(f"R$ {valor_produto:.2f}")

elif forma_pagamento == "Cartão":
    funcao_cartao = input("Informe o tipo de pagamento por cartão (Débito/Crédito): ")

    if funcao_cartao == "Crédito":
        parcelas = int(input("Informe a quantidade de parcelas (01/02/03): "))
        parcelas_finais = valor_produto/parcelas

        if parcelas > 3:
            print("Quantidade de parcelas inválida")
        else:
            print(f"R$ {valor_produto:.2f}")
            print(f"{parcelas} parcelas de R$ {parcelas_finais:.2f}")
    
    else:
        print(f"R$ {valor_produto:.2f}")

else:
    print(f"R$ {valor_produto:.2f}")
