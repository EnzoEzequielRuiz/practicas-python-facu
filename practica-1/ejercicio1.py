'''Escribir en papel, separando con una flecha (->), cada paso de las reducciones de las siguientes expresiones matematicas hasta hallar el valor final al cual se reducen.
(Ejemplo: 2 + 3 * 5 (->) 2 + (3*5) (->) 2 + 15 (->) 17'''

uno = 20 + 12 * 13
# 20 + (12*13) (->) 25 * 156 = 3120

dos = 17 / 15 + 30
# (17/15) + 30 (->) 1.13 + 30 = 31.13

tres = 17 / 15 * 30
# (17/15) * 30 (->) 1.13 * 30 = 34

cuatro = (17/15) * 30
# 1.13 * 30 = 34

print(uno,dos,tres,cuatro)