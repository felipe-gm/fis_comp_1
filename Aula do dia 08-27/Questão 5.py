#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import loadtxt

x = loadtxt('similaridade_Terra.txt')

w = [0.57, 1.07, 0.7, 5.58]

corpos_celestes = [
    'Terra',
    'Marte',
    'Mercurio',
    'Lua',
    'Venus',
    'Io',
    'Jupiter',
    'Tita',
    'GJ 581 g',
    'GJ 581 b',
    'HD 96167 b',
    'WASP-26 b'
]

IST = {}

for j in range(len(corpos_celestes)):
    ISTj = 1
    for i in range(len(w)):
        ISTj *= (1 - abs((x[j][i]-x[0][i])/(x[j][i]+x[0][i])))**(w[i]/len(w))
    
    IST[corpos_celestes[j]] = ISTj


# In[2]:


print(IST)
print()


# In[3]:


print(f'''
O corpo celeste mais semelhante a Terra eh:
{sorted(IST, key=IST.get, reverse=True)[1]}
''')

