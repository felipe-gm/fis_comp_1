#!/usr/bin/env python
# coding: utf-8

# In[1]:


primos = [2]

for n in range(3, 100):
    for s in primos:
        if s>n**(1/2): 
            primos.append(n)
            break
            
        elif n%s==0: break

print(primos)

