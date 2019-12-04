#!/usr/bin/env python
# coding: utf-8

# por Felipe Miyazato

# In[1]:


def intersect_bin_search(func_0, func_1, inf, sup, eps=0.001):
    """Given two monotone function (func0, func1: float -> float) over the
    iterval [inf, sup] (inf, sup in float) returns inferred coordinate of
    istersenction with precision eps.
    
    Positional arguments:
    func_0, func_1 -- monotone function over [inf, sup]
    inf -- lower bound of search interval
    sup -- upper bound of search interval
    
    Keyword arguments:
    eps -- precision required for the result (default .001)
    """
    
    delta_inf = func_1(inf) - func_0(inf)
    delta_sup = func_1(sup) - func_0(sup)
    
    # No intersection here
    if delta_inf * delta_sup > .0: return None 
    
    # Exact solution found?!?
    if delta_inf == .0: return inf
    if delta_sup == .0: return sup

    avg = (sup + inf)/2
        
    # Did I dug enough?
    if sup-inf <= eps: return avg
        
    # Keep trying
    return intersect_bin_search(func_0, func_1, inf, avg)        or intersect_bin_search(func_0, func_1, avg, sup)


# In[2]:


def six_lwr_lvls(w=1e-9, V=20, eps=0.001):
    """Finds up to six lower possible energy levels for an electron in a
    squared potential of width (w) and heigth (V), on precision eps.    
    
    Keyword arguments:
    w -- width of potential (default 1e-9)
    V -- heigth of potential (default 20)
    eps -- precision required for the result (default .001)
    """
    
    from math            import pi
    from scipy.constants import physical_constants
    from Item_a          import func_0, func_1, func_2

    h_ = physical_constants['Planck constant over 2 pi in eV s'][0]
    m  = 9.1094e-31 / physical_constants['electron volt'][0] # massa do elétron
    
    i = 0
    n_lvls = 0
    intersections = {}
    
    while i < 6:
        # define interval of search by exploring tan singularities
        arg_tan_inf = -pi/2 + pi*((i+1)//2) if -pi/2 + pi*((i+1)//2)>0 else 0
        arg_tan_sup =  pi/2 + pi*((i+1)//2)
        i += 1

        # define closed compact to search for E
        E_inf = arg_tan_inf**2 * 2 * h_**2 / (w**2 * m) + eps**2
        E_sup = arg_tan_sup**2 * 2 * h_**2 / (w**2 * m) - eps**2
        
        if E_inf > V: break
        if E_sup > V: E_sup = V - eps**2
        
        # parametrize theoretic functions
        func_0_w = lambda x: func_0(x, omega=w)
        func_1_w = lambda x: func_1(x,     V=V)
        func_2_w = lambda x: func_2(x,     V=V)

        if n_lvls%2==0: # indice par
            val = intersect_bin_search(func_0_w, func_2_w, E_inf, E_sup)
            # found it?
            if val is None:
                print(
                    f'''Sem interseccoes pares no intervalo [{E_inf}, {E_sup}],
dada precisao {eps}'''
                )
            # found it!
            else: 
                n_lvls += 1
                intersections[f'E_{i}'] = val
            
        else: # indice impar
            val = intersect_bin_search(func_0_w, func_1_w, E_inf, E_sup)
            # found it?
            if val is None:
                print(
f'''Sem interseccoes impares no intervalo [{E_inf}, {E_sup}],
dada precisao {eps}'''
                )
            else:
                n_lvls += 1
                intersections[f'E_{i}'] = val
    
    return intersections


# In[3]:


def main():
    print('Seis primeiros níveis de energia:')
    print(six_lwr_lvls())
    
if __name__ == "__main__":
    main()

