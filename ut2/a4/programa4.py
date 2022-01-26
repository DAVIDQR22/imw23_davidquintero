import sys

imput_num = sys.argv[1:]
quantity_num = len(imput_num)
num_summary = 0

for i in imput_num:
    i=float(i)
    num_summary+=i
result = num_summary / quantity_num
print(f"La media de los valores es: {result}")
