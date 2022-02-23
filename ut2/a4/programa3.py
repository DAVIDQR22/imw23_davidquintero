import sys

input_num = int(sys.argv[1])
chain = sys.argv[2]
word, count = 0, 0
chain = chain + ' '

if input_num <= 0:
 sys.exit('Introduzca un número positivo, por favor.')
else:
 for char in chain:
     if char != ' ':
        count += 1
     else:
         if count == input_num:
            word += 1
            count = 0
         else:
             count = 0
print(f'Hay {word} palabras de tamaño {input_num}')
