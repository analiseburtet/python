A = int(input('Digite um numero: '))
B = int(input('Digite um numero: '))
C = int(input('Digite um numero: '))

def findLesserValue():
    numbers = [A,B,C]
    numbers.sort()
    return numbers[0]

print(findLesserValue())