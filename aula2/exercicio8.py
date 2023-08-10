def notaGrauA():
  return round(praticaA * 0.33 + teoricaA * 0.67, 2)

def notaGrauB():
  return round(lab * 0.6 + teorico * 0.2 + trabalho * 0.2, 2)

def notaFinal():
  return round(notaGrauA() * 0.33 + notaGrauB() * 0.67, 2)

print('Vamos começar a calcular sua nota final, primeiro informe as notas do grau A')
praticaA = float(input('Digite sua nota da atividade pratica: '))
teoricaA = float(input('Digite sua nota da atividade teorica: '))

print('Sua nota do grau A é:', notaGrauA())
print('Agora informe suas notas do grau B')
lab = float(input('Digite sua nota do laboratorio: '))
teorico = float(input('Digite sua nota teorica: '))
trabalho = float(input('Digite sua nota do trabalho: '))
print('Sua nota do grau B é: ', notaGrauB())

print('Sua nota final é: ', notaFinal())