#!/usr/bin/env python
# coding: utf-8

# In[1]:


def particle_M_contrib(i,j,k):
    """
    https://en.wikipedia.org/wiki/Madelung_constant
    """
    if i==0 and j==0 and k==0: return 0
    
    return ( (-1)**(i+j+k) ) / ( ((i**2) + (j**2) + (k**2))**(1/2) )

L = 175

M = 0
for i in range(-L, L):
    for j in range(-L, L):
        for k in range(-L, L):
            M+=particle_M_contrib(i,j,k)
            
print(f'A constante de Madelung para o cloreto de sódio é: {M}')

