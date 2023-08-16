year = int(input('Digite um ano: '))

def isLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print('ano informado é bissexto')
    else:
        print('ano informado nao é bissexto')

isLeapYear(year)
