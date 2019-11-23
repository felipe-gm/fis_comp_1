#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import DataFrame, Series

import matplotlib.pyplot as plt
import numpy as np
#get_ipython().run_line_magic('matplotlib', 'inline')

Ns = [n for n in range(50,1501,50)]

def f(x): return (1-x**2)**(1/2)

def sum_f(N): 
    s = 0.
    for x in np.linspace(-1,1,N):
        s += f(x)*2/N
    return s

def integr_f(): return np.pi/2

re_intgr = [sum_f(n) for n in Ns]

DataFrame(
    data=re_intgr,
    index=Series(data=Ns, name='N'),
    columns=['re_intgr'],
).to_csv(f'2-tabela_com_os_valores.csv')


# In[2]:


plt.scatter(Ns, re_intgr)
plt.plot([Ns[0],Ns[-1]],[integr_f(),integr_f()],'r')
plt.xlabel('Pontos (N)')
plt.ylabel(f'integral de f(x)dx entre -1 e 1')
plt.savefig(f'3-grafico.png')

