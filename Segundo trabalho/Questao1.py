#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pylab import plot, scatter, xlabel, ylabel, xlim, ylim, show
from numpy import linspace

N = 1000

X = linspace(-2, 2, N, endpoint=True)
Y = linspace(-2, 2, N, endpoint=True)

iter_qtt = 100

mandel_subsetX = []
mandel_subsetY = []

for x in X:
    for y in Y:
        c = x + 1j*y
        z = c
        
        for _ in range(iter_qtt):
            z = z**2 + c
            
            if abs(z)>=2: break
            
        if abs(z)<2:
            mandel_subsetX.append(x)
            mandel_subsetY.append(y)

scatter(mandel_subsetX, mandel_subsetY, s=.01, c='k')
show()
