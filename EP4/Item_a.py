#!/usr/bin/env python
# coding: utf-8

# por Felipe Miyazato

# In[1]:


def func_0(E_i, omega=1e-9):
    """Calculates the result for the equation:
    tan(sqrt((omega^2 * m * E_i)/(2 * h_^2)))
    
    Positional arguments:
    E_i -- energy in eV
    
    Keyword arguments:
    omega -- largura do poco potencial em metros (default 1e-9)
    """
    
    from numpy import tan
    from scipy.constants import physical_constants
    
    m  = 9.1094e-31 / physical_constants['electron volt'][0] # massa do elétron
    h_ = physical_constants['Planck constant over 2 pi in eV s'][0]

    return tan((omega**2 * m * E_i / (2 * h_**2))**(1/2))

def func_1(E, V=20): 
    """Calculates the result for the equation:
    -sqrt((E)/(V - E))
    
    Positional arguments:
    E -- energy in eV
    
    Keyword arguments:
    V -- profundidade do potencial em eV (default 20.)
    """
    
    return -(E / (V - E))**(1/2)

def func_2(E, V=20):
    """Calculates the result for the equation:
    sqrt((V - E)/(E))
    
    Positional arguments:
    E -- energy in eV
    
    Keyword arguments:
    V -- profundidade do potencial em eV (default 20.)
    """
    
    return  ((V - E) / E)**(1/2)


# In[2]:


def do_plot(omega=1e-9, V=20):
    """Plota os graficos de func_0, func_1 e func_2 sobrepostos e 
    parametrizados em omega e V.
    
    Keyword arguments:
    V -- profundidade do potencial em eV (default 20.)
    omega -- largura do poco potencial em metros (default 1e-9)
    """

    from pylab import plot, show, ylim, xlabel, legend, xticks
    from numpy import linspace, arange
    
    x = linspace(0, V, 1000)

    plot(x, func_0(x, omega), label='E_i'    )
    plot(x, func_1(x,     V), label='E_impar')
    plot(x, func_2(x,     V), label='E_par'  )
    
    xlabel('E (eV)')
    xticks(arange(0, V+1, round(V/20)))
    ylim(-10,10)
    legend(loc = 'upper right')
    
    show()


# In[3]:


def main():
    do_plot()
    
if __name__ == "__main__":
    main()


# Estimativas visuais:
#  - E_1: 0.3 eV,
#  - E_2: 1.3 eV, 
#  - E_3: 2.9 eV,
#  - E_4: 5.1 eV, 
#  - E_5: 7.9 eV, 
#  - E_6: 11.2 eV
