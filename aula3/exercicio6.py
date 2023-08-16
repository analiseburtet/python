price = float(input('Digite um numero: '))

if price < 0:
    print('erro')
elif price < 100:
    print(price*1.1)
elif price < 300:
    print(price*1.2)
elif price < 1000:
    print(price*1.5)
else:
    print(price)
