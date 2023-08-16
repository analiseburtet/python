print('Digite 1 para somar dois valores')
print('Digite 2 para subtrair dois valores')
print('Digite 3 para multiplicar dois valores')
print('Digite 4 para dividir dois valores')
print('Digite 5 para realizar uma potência entre dois valores')
print('Digite 6 para realizar uma radiciação entre dois valores')
print('Digite qualquer outro número para sair')

number = int(input(''))
if (number >=1) and (number <=6):
   a = int(input('Digite um valor: '))
   b = int(input('Digite um valor: '))

match number:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a*b)
    case 4:
        print(a/b)
    case 5:
        print(a**b)
    case 6:
        print(a**1/b)
        