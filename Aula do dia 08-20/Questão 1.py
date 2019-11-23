#!/usr/bin/env python
# coding: utf-8

from numpy import array

i              = 1
not_4_multiple = []
while i<=100:
    if i%4 != 0: # verifica se eh divisivel por 4
        not_4_multiple.append(i)
    i+=1
    
not_4_multiple = array(not_4_multiple)
print('O array de de nao multiplos de 4 é:')
print(not_4_multiple)

print('O tamanho deste array é: '+str(not_4_multiple.__len__()))

sqrt = not_4_multiple**(1/2)

add = not_4_multiple+sqrt

su = add.sum()

print('O resultado da soma dos elementos do terceiro vetor é: '+str(su))

