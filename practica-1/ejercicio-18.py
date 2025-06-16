'''
Escribir un programa en Python que pida al usuario una cantidad de segundos y muestre en pantalla la cantidad de dias, minutos y segundos que representa. Por ejemplo, si el usuario ingresa 86461 segundos el programa debe mostrar por pantalla: 1 dia, 0 horas, 1 minuto, 1 segundo.
'''

cantidad_segundos = int(input('Ingrese la cantidad de segundos, para saber cuanto equivale a dias, horas, minutos y segundos: '))
s = 1
m = 60 * s
hs = 60 * m
d = 24 * hs

cant_d = cantidad_segundos // d
res_d = cantidad_segundos % d
cant_hs = res_d // hs
res_hs = res_d % hs
cant_m = res_hs // m
res_m = res_hs % m
cant_s = res_m // s

print(cantidad_segundos,'son',cant_d,'dias,',cant_hs,'horas,',cant_m,'minutos,',cant_s,'segundos.')