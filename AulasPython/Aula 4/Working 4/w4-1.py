def operacao(n1, n2, operador):
    if operador[0] == '+':
        resultado = n1 + n2
    elif operador[0] == '-':
        resultado = n1 - n2
    elif operador[0] == '*':
        resultado = n1 * n2
    elif operador[0] == '/':
        resultado = n1 / n2
    return resultado

n1, operador, n2 = float(input()), input(), float(input())

resultado = operacao(n1, n2, operador)

print('{:.1f}'.format(resultado))
