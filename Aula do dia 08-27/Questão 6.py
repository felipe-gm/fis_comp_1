#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fatorial_dupla(n):
    if n<=1: return 1
    else:    return n*fatorial_dupla(n-2)


# In[2]:


for n in range(20):
    print(f'{n+1}!! = {fatorial_dupla(n+1)}')

