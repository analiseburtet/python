price = float(input('Digite o preco do produto: '))

if price <= 0:
    print('Preço inválido')
elif price <= 30:
    print('Preço baixo')
elif price <= 50: 
    print('Preço médio')
else:
    print('Preço alto')
