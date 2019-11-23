# formula (3) em Latex:
#     h = G \left( \frac{MT^2}{4 \pi ^2} \right) ^{\frac{1}{3}} - R

from math import pi

G = 6.67e-11 # constante gravitacional de Newton em (m^2 kg^-1 s^-2)
M = 5.97e24  # massa da Terra em (kg)
R = 6371     # raio medio da Terra em (km)

print('''Um satélite deve ser lançado em uma órbita circular em torno da
Terra, de forma que complete uma volta ao redor do planeta a cada T
segundos.''')
T = int(input('Digite valor desejado de T: ')) 

R = R*1000 # correcao do raio medio da Terra para (m)

print('A altitude correta em metros é:')
print((G*M*T**2/(4*pi))**(1/3) - R) # aplicacao da fórmula (3)
