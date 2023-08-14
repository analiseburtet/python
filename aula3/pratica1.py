X = float(input('Digite um número: '))
Y = int(input('Digite um número: '))

def multiply():
    return X * Y

def divide():
    return round(X / Y, 2)

def potency():
    return X ** Y

divideResult = divide()
print('X multiplicado por Y é: ', multiply())
print('X dividido por Y é: {}, mas com apenas 2 casas decimais é {:.2f}'.format(divideResult, divideResult))
print('X elevado a Y é: ', potency())