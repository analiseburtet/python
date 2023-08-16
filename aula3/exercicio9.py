grauA = float(input("Digite a nota do Grau A: "))
grauB = float(input("Digite a nota do Grau B: "))

def isGrauCRequired():
    if ((grauA * 0.33) + (grauB * 0.67)) >= 6:
        return "Aprovado"
    else:
        return "Necessita fazer Grau C"

print(isGrauCRequired())