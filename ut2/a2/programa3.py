import sys
import math

nota = float(sys.argv[1])

if nota < 0 or nota > 10:
    print('Error. El valor introducido no es un número válido.')

else:
    if nota < 5:
        print('Suspenso')
    elif nota >= 5 and nota < 7:
        print('Aprobado')
    elif nota >= 7 and nota < 9:
        print('Notable')
    elif nota >= 9 and nota < 10:
        print('Sobresaliente')
    elif nota == 10:
        print('Matrícula de honor')
