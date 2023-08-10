trabalho = float(input('Digite sua nota do trabalho: '))
prova = float(input('Digite sua nota da prova: '))
teste = float(input('Digite sua nota do teste: '))

def notaFinal():
  return round(trabalho * 0.1 + prova * 0.6 + teste * 0.3 , 2)

print('Sua nota final é: ', notaFinal())