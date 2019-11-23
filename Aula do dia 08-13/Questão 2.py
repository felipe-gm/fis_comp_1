#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import pi
h = 4.135667662e-15 # constante de Planck em (eV s)

m     = 9.11e-31 # massa do eletron em kg
E     = 10       # energia do eletron em eV
h_bar = h/(2*pi) # constante reduzida de Planck
V     = 9        # barreira potencial em eV

k_1 = (2*m*E)**(1/2) / h_bar
k_2 = (2*m*(E-V))**(1/2) / h_bar

T = 4*k_1*k_2/((k_1+k_2)**2)
R = ((k_1-k_2)/(k_1+k_2))**2

print(f'A probabilidade de tranmissao e: {T}')
print(f'A probabilidade de reflexao e: {R}')

