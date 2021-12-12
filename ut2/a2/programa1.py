import sys
import math
from math import sqrt

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if b ** 2 - 4 * a * c < 0:
    print ('Esta ecuación no tiene una solución real.')

elif a == 0:
    x = -c / b
    print ('x =', x)
else:
    x1 = (-b + sqrt (b ** 2 -4 * a * c)) / 2 * a
    x2 = (-b - sqrt (b ** 2 -4 * a * c)) / 2 * a
    print('x1 =', x1, 'x2 =', x2)

