#!/usr/bin/env python
# coding: utf-8

# In[1]:


def R_H(v0=10, alpha=30):
    '''
R_H(v0=10, alpha=30)

Calcula em unidades do S.I. o alcance (R) e a altura maxima (H) de um
projetil lancado a partir do solo, em um terreno horizontal, desprezando
a resistencia do ar e a curvatura da Terra.

    H = (v0*sin(alpha))**2 / (2*g)
    
    R = (v0*sin(2*alpha))**2 / g

Parameters
----------
v0: float
    Magnitude da velocidade de lancamento, em m/s.
alpha: float
    Angulo de lancamento em graus.
    
Returns
-------
y : tuple (float, float)
    Em unidades do SI, y[0] o alcance R e y[1] a maxima altura H de um
    projetil lancado a partir do solo, em um terreno horizontal,
    desprezando a resistencia do ar e a curvatura da Terra.

Notes
-----
https://alunosonline.uol.com.br/fisica/lancamento-obliquo.html
https://www.iag.usp.br/~eder/agg0115/o_campo_de_gravidade_terrestre_AGG0115_2019.pdf

Examples
--------
Print sine of one angle:

>>> R_H()
(7.66368583008094, 1.2772809716801565)
    '''
    from math import pi, sin
    
    g = 9.7864137
    alpha = alpha*pi/180
    
    return (v0*sin(2*alpha))**2/g, (v0*sin(alpha))**2/(2*g)

print(f'''
Para v0=10 m/s e alpha=30 graus os resultados sao:
    R = {R_H(v0=10, alpha=30)[0]} m
e
    H = {R_H()[1]} m
    ''')

