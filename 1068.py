while True:
    try:

        M = input()

        qtd = 0

        for j in M:
            if j == '(':
                qtd += 1
            elif j == ')':
                qtd -= 1

            if qtd < 0:
                break

        if qtd == 0:
            print('correct')
        else:
            print('incorrect')

    except EOFError:
        break