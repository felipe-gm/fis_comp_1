#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandas import DataFrame, Series

import matplotlib.pyplot as plt
import numpy as np
#get_ipython().run_line_magic('matplotlib', 'inline')

x0 = float(input('Ponto onde calcular a derivada (x0): '))

deltas = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10, 1e-12, 1e-14]

def f(x): return x*(x-1)

def diff_f(x, delta): return (f(x+delta)-f(x))/delta

def deriv_f(x): return 2*x-1

df_dx = [diff_f(x0, delta) for delta in deltas]

DataFrame(
    data=df_dx,
    index=Series(data=deltas, name='delta'),
    columns=['diferenca'],
).to_csv(f'2-tabela_com_os_valores-x0={x0}.csv')


# In[2]:


plt.xscale('log')
plt.scatter(deltas, df_dx)
plt.plot([deltas[0],deltas[-1]],[deriv_f(x0),deriv_f(x0)],'r')
plt.xlabel('dx')
plt.ylabel(f'df({x0})/dx')
plt.savefig(f'3-grafico-x0={x0}.png')

