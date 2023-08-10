import math

A = int(input('Digite um número inteiro: '))
B = int(input('Digite um número inteiro: '))
C = int(input('Digite um número inteiro: '))
D = int(input('Digite um número inteiro: '))
E = int(input('Digite um número inteiro: '))

def area():
    return (B * C) / 2

def perimeter():
    return A + B + C + D

def radius():
    return math.pi * E ** 2

print('A area do triangulo é: ', area())
print('O perimetro do retangulo é: ', perimeter())
print('A area do circulo é:', radius())