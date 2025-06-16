'''
-Determinar cuantos segundos tiene una hora, y cuantos segundos tiene un dia.
-Escribir una expresion matematica que transforme un lapso de tiempo expresado en segundos a uno expresados en minutos.
-Escribir otra para transformar a horas y una ultima que transforme en dias.
-Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre cuantos minutos son, asi tambien cuantas horas y cuantos dias.
'''

#Dia y hora expresados en segundos
seg = 1
min = 60 * seg
hs = 60 * min
dia = 24 * hs
print('Cuantos segundos tiene un dia: ',dia,'\nCuantos segundos tiene una hora: ',hs)

#Dia y hora expresados en minutos
min = 1
hs = 60 * min
dia = 24 * hs
print('La cantidad de minutos que tiene un dia: ',dia,'\nLa cantidad de minutos que tiene una hora: ',hs)


