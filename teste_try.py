def leiaInt(num):

    try:
        n = int(input(num))
    except ValueError:
        print("O número informado não é inteiro")
    except KeyboardInterrupt:
        print("Não foi digitado nenhum valor")
    else:
        print(f"O número informado foi {n}")
    
        return n

leiaInt("Informe um valor: ")