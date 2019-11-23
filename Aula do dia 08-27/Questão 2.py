#!/usr/bin/env python
# coding: utf-8

# # Isotopo mais estavel

# In[1]:


def B(Z, A):
    a1, a2, a3, a4 = 15.8, 18.3, 0.714, 23.2
    if   A%2==1: a5 =    .0
    elif Z%2==0: a5 =  12.0
    else       : a5 = -12.0
        
    return (
        a1*A - a2*A**(2/3)     - a3*Z*(Z-1)/A**(1/3)
             - a4*(A-2*Z)**2/A + a5/A**(1/2)
    )

mtrz_BpA = [[-1],] # inicia alista que vai reter os valores de B/A (M[Z][A-Z])
                   # a primeira entrada é [-1] pois não temos Z=0
for Z in range(1, 101):
    ls_BpA = []
    for A in range(Z,3*Z+1):
        ls_BpA.append(B(Z, A)/A)
        
    A_est = ls_BpA.index(max(ls_BpA))+Z
    
    print(f'Para Z = {Z}:')
    print(f' - O valor de A do nucleo mais estavel eh {A_est}')
    print(f' - O valor correspondente de ligacao por nucleon eh {max(ls_BpA)}')
    
    mtrz_BpA.append(ls_BpA)


# # Atomo mais estavel

# In[2]:


best_BpA = [max(ls_BpA) for ls_BpA in mtrz_BpA]

print(f'''
Para Z igual a {best_BpA.index(max(best_BpA))} tem-se o maior valor de B/A
''')


# # Teste Z=28 e A=58

# In[3]:


print(f'''
A energia de ligacao B para o caso em que Z=28 e A=58 eh {B(28, 58)}, da
ordem de 500MeV.
''')


# # Teste Z=80, isotopo mais estável

# In[4]:


BpA_80 = mtrz_BpA[80]
stableA_Z80 = BpA_80.index(max(BpA_80))+80

print(f"""
O elemento de numero atomico 80 tem o isotopo de massa {stableA_Z80} 
como mais estavel e sua energia por nucleon eh de aproximadamente 
{max(mtrz_BpA[80])} MeV.
""")

