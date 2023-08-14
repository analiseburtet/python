a = int(input('Informe A: '))
b = int(input('Informe B: '))
c = int(input('Informe C: '))


def baskaraPlus():
    top = -b + (((b**2) -(4*a*c)))** (1/2)
    base = 2 * a

    return top/base

def baskaraMinus():
    top = -b - (((b**2) -(4*a*c)))** (1/2)
    base = 2 * a

    return top/base

print("x’ é a raíz positiva", baskaraPlus())
print("x’’ é a raíz negativa", baskaraMinus())