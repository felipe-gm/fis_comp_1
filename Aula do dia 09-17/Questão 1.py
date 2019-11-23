#!/usr/bin/env python
# coding: utf-8

# # Atomos de um unico cubo na origem

# ## Atomos dos vertices

# $$
# (0, 0, 0)
# $$
# $$
# (1, 0, 0), (0, 1, 0), (0, 0, 1)
# $$
# $$
# (0, 1, 1), (1, 0, 1), (1, 1, 0)
# $$
# $$
# (1, 1, 1)
# $$

# ## Atomos das faces

# $$
# (0, 0.5, .5), (0.5, 0, 0.5), (0.5, 0.5, 0)
# $$
# $$
# (1, 0.5, 0.5), (0.5, 1, 0.5), (0.5, 0.5 1)
# $$

# # Visualizacao de uma rede CFC

# In[1]:


from vpython import sphere, vector, color

L=int(input('Quantos cubos na rede cristalina? '))
R = 0.1
print()
print('''
Em verde indicamos os atmos posicionados nos vertices dos cubos
''')
for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            sphere(pos=vector(i,j,k), radius=R, color=color.green)
            
print('''
Em azul indicamos os atmos posicionados nos centros das faces dos cubos
''')
for i in range(-L, L+1):
    for j in range(-L, L):
        for k in range(-L, L):
            sphere(pos=vector(i,j+.5,k+.5), radius=R, color=color.blue)
            
for i in range(-L, L):
    for j in range(-L, L+1):
        for k in range(-L, L):
            sphere(pos=vector(i+.5,j,k+.5), radius=R, color=color.blue)
            
for i in range(-L, L):
    for j in range(-L, L):
        for k in range(-L, L+1):
            sphere(pos=vector(i+.5,j+.5,k), radius=R, color=color.blue)

