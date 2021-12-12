import sys
import math
from math import pi

r = float(sys.argv[1])

print('(1) Calcular el diámetro de la circunferencia.')
print('(2) Calcular el perímetro de la circunferencia.')
print('(3) Calcular el área del círculo.')
print('(4) Salir.')

menu = int(input('Seleccione algunas de las opciones: 1 - 4. '))

if menu < 1 or menu > 4:
    print('Error. Por favor, introduzca un valor asignado a alguna de las opciones.')

else:
    if menu == 1:
        d = 2 * r
        print('Diámetro:', d)
    elif menu == 2:
        p = 2 * pi * r
        print('Perímetro:', p)
    elif menu == 3:
        a = pi * r ** 2
        print('Área:', a)
    elif menu == 4:
        sys.exit()
