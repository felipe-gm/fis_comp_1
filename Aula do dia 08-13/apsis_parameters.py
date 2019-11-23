from math import pi
M = 1.9891e30
G = 6.6738e-11

l_1 = float(input('Valor da distancia ao Sol no perielio em metros: '))
v_1 = float(input('''Valor da velocidade de translacao no perielio em
m/s: '''))

v_2 = 2*G*M/(v_1*l_1) - v_1
l_2 = l_1*v_1/v_2

a = (l_1+l_2)/2
b = (l_1*l_2)**(1/2)

T   = 2*pi*a*b/(l_1*v_1)
e   = (l_2-l_1)/(l_2+l_1)

print(f'l_2 = {l_2}m')
print(f'v_2 = {v_2}m/s')
print(f'T = {T}s')
print(f'e = {e}')