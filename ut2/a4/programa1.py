import sys

dni = int(sys.argv[1])
letter = 'TRWAGMYFPDXBNJZSQVHLCKE'
remain = dni%23
print(f'{dni}{letter[remain]}')
