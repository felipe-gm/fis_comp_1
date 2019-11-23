#!/usr/bin/env python
# coding: utf-8

# ## Definicoes

# ### Metodos de integracao

# In[1]:


from math import pi

def finite_integration(f, frm=0.0, to=pi, method='simpson', N=60):
    """Calculates finite integration of a function (f) inside given interval
    by either Simpson method or Gaussian quadrature
    
    Positional arguments:
    f -- function to integrate (type function)
    
    Keyword arguments:
    frm -- lower bound of integration (default 0.0)
    to -- upper bound of integration (default pi)
    method -- method of numeric integration to run [options 'simpson',
    'gauss'] (default 'gauss')
    n -- number of samples to use (defualt 60)
    """
    
    # Simpson method case
    if method=='simpson':
        terms = [] # to feed with simpsons formula sum terms
        delta_x = (to-frm)/N
        
        # 1st term caculation
        terms.append(delta_x*(f(frm)+f(to))/3)
        
        # 2nd term caculation
        s, k= 0.0, 1
        while k<=N-1:
            s += f(frm + k*delta_x)
            k += 2
        terms.append(4*delta_x*s/3)
        
        # 3rd term caculation
        s, k= 0.0, 2
        while k<=N-2:
            s += f(frm + k*delta_x)
            k += 2
        terms.append(2*delta_x*s/3)
        
        return sum(terms)
    
    # Gaussian quadrature case
    if method=='gauss':
        from gaussxw import gaussxwab
        
        # Calculates os samples nd weights inside [frm, to] interval
        x, w = gaussxwab(N, frm, to)
        
        # Does summation
        s = 0.0
        for k in range(N):
            s += w[k] * f(x[k])
            
        return s


# ## Funcao de Bessel

# In[2]:


def bessel(x, m, meth_int='simpson'):
    """Calculates m-order Bessel's function, valuated on x by given method of
    integration (meth_int)
        
    Positional arguments:
    x -- point to evaluate m-order Bessel's function (type float)
    m -- order of Bessel's function to calculate (type int)
    
    Keyword arguments:
    meth_int -- method of numeric integration to run [options 'simpson',
    'gauss'] (default 'gauss')
    """
    
    from math import pi
    
    def integrand(theta):
        from math import cos, sin
        return cos(m*theta - x*sin(theta))
    
    return finite_integration(integrand, method=meth_int)/pi


# # Calcular

# In[3]:


from numpy import linspace

x = linspace(0, 20, 100)
J = [{'simpson': [], 'gauss': []} for dummy in range(3)]

for t in x:  # "para x variando de 0 a 20, com 100 pontos"
    for idx, jn in enumerate(J): # para J0(x), J1(x) e J2(x)
        for key in jn: # "com o metodo de Simpson e de quadratura Gaussiana."
            jn[key].append(bessel(t, idx, meth_int=key)) # calcular


# # Graficar

# In[4]:


def main():
    from pylab import xlabel, ylabel, plot, legend, show

    xlabel('x')
    ylabel('Jm(x)')
    color_schema = [
        {'simpson': 'r', 'gauss': 'r'},
        {'simpson': 'g', 'gauss': 'g'},
        {'simpson': 'b', 'gauss': 'b'}
    ]

    for m, j in enumerate(J):
        for key in j:
            lbl = 'J'+str(m)+'_'+str(key)
            plot(x, j[key], color_schema[m][key], label=lbl) # graficar

    legend(loc = 'upper right')
    show()
    
if __name__ == "__main__":
    main()

