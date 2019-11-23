#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import array

sig_x = array(
    [
        [0+0j,  1+0j],
        [1+0j,  0+0j]
    ]
)
sig_y = array(
    [
        [0+0j,  0-1j],
        [0+1j,  0+0j]
    ]
)
sig_z = array(
    [
        [1+0j,  0+0j],
        [0+0j, -1+0j]
    ]
)
print('A matriz sigma x é:')
print(sig_x)
print('A matriz sigma y é:')
print(sig_y)
print('A matriz sigma z é:')
print(sig_z)

def comut(m0, m1):
    from numpy import dot
    return dot(m0, m1) - dot(m1, m0)
result = comut(sig_x,sig_y)/2j, comut(sig_y,sig_z)/2j, comut(sig_z,sig_x)/2j
print('Resultados:')
print(result[0])
print(result[1])
print(result[2])

