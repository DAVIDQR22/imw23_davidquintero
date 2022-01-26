import random

NUCLEOBASES = "ATGC"
DNA_SIZE = 100
a, t, g, c = 0, 0, 0, 0

sequence = ''.join([random.choice(NUCLEOBASES) for i in range(DNA_SIZE)])
for nucleotide in sequence :
 if nucleotide == 'A':
  a+=1
 elif nucleotide == 'T':
  t+=1
 elif nucleotide == 'G':
  g+=1
 elif nucleotide == 'C':
  c+=1
out = f'''Adenine: {a}
Guanine: {g}
Cytosine: {c}
Thymine {t}'''
print(out)
