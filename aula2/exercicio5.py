i = 0
numbers = []

def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

def multiply(numbers):
  total = 1
  for number in numbers:
    total *= number
  return total

while i < 5:
  number = int(input('Digite um número inteiro: '))
  numbers.append(number)
  i += 1

print("A soma dos números é:", sum(numbers))
print("O produto dos números é:", multiply(numbers))
