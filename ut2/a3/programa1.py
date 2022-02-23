import sys
num = int(sys.argv[1])
if num <= 0:
    sys.exit('Por favor, introduzca un valor positivo.')
else:
    for value in range(2, num):
        if num % value == 0:
            print ('No es primo!')
            break
    else:
        print ('Es primo!')
