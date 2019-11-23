#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from vpython import sphere , vector, color, rate
from math    import cos    , sin   , pi
from numpy   import loadtxt, arange

# ajustando a visualizacao

colors = [
    color.orange,
    color.magenta,
    color.blue,
    color.red,
    color.green,
    color.purple,
    color.yellow
]

c1_ls = [
    3e-4,
    3e-4,
    3e-4,
    3e-4,
    3e-4,
    3e-4,
    5e-5
]


# constantes

dia = 24*60*60
tmax = 1e4*dia
dt = dia

orb_params = loadtxt('orbitas.tsv')

col_dict = {'r_obj':0,'r_orb':1,'p':2}

omega_p = 2*pi/dia

# objetos

objs = [None for i in range(7)]
for idx, row in enumerate(orb_params[:-1]):
    objs[idx] = sphere(
        pos=vector(orb_params[idx][col_dict['r_orb']], 0, 0),
        radius=orb_params[idx][col_dict['r_obj']]*c1_ls[idx],
        color=colors[idx]
    )
objs[6] = sphere(
    pos=vector(0, 0, 0),
    radius=orb_params[6][col_dict['r_obj']]*c1_ls[6],
    color=colors[idx]
)

    
# laco da animacao

for t in arange(0, tmax, dt):
    rate(20)
    for idx, row in enumerate(orb_params[:-1]):
        r_orb = orb_params[idx][col_dict['r_orb']]
        x = r_orb*cos(omega_p*t/orb_params[idx][col_dict['p']])
        y = r_orb*sin(omega_p*t/orb_params[idx][col_dict['p']])
        objs[idx].pos = vector(x, y, 0)

