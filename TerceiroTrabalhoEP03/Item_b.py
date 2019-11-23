#!/usr/bin/env python
# coding: utf-8

# # Definicoes preliminares

# In[1]:


def I_polar(r, lmbd=400e-9):
    """Gives light intensity of a circular diffraction pattern
    I(r) = (J1(kr)/(kr))^2
    r for distance from center of focal plane, k=2*pi/lmbd nd J1 is Bessel's
    function of order 1.
    
    Positional arguments:
    r -- distance from center of focal plane (type float)
    
    Keyword arguments:
    lmbd -- light wavelenght (default 400e-9)
    """
    from Item_a import bessel
    from math   import pi
    
    k = 2*pi/lmbd
    
    return (bessel(k*r,1)/(k*r))**2


def I_cartesian(x, y, lmbd=400e-9):
    """Cartesian wraper for I(r) assuming (0, 0) as center of focal plane.
    
    Positional arguments:
    x, y -- cartesian coordinates (type float, float)
    """
    return I_polar((x**2+y**2)**(1/2), lmbd)


# # Script

# In[2]:


def main(log_scaling=False, lmbd=400e-9):
    from numpy import linspace
    from pylab import imshow, hot, show
    from math import log

    # "...gerar a intensidade da luz no padrao de difracao circular..."
    data = []
    for x in linspace(-1e-6, 1e-6, 100):
        Y = []

        for y in linspace(-1e-6, 1e-6, 100):
            if log_scaling: Y.append(log(I_cartesian(x, y, lmbd=lmbd)))
            else: Y.append(I_cartesian(x, y, lmbd=lmbd))
        
        data.append(Y)
        
    imshow(data) # "...fazer o grafico..."
    hot() # "...com o esquema de cores "hot"..."
    show()

if __name__ == "__main__":
    main()

