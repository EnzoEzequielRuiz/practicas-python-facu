'''
Una empresa telefonica desea un programa para calcular el importe de sus clientes. Sabiendo que el costo por comunicacion es de $12 y por cada segundo se cobra $1.5 hacer dicho programa.
Se deben ingresar la cantidad de llamadas realizadas y el tiempo total de comunicacion, el programa debe devolver el precio a cobrar. Por ejemplo, si realizo 10 llamadas con un total de 4000 segundos el importe a pagar seria de $6120
'''

costo_por_comunicacion = 12
costo_por_segundos = 1.5

cantidad_de_llamas = int(input('Ingrese la cantidad de llamas realizadas: '))
tiempo_total_de_llamadas = int(input('Ingrese el tiempo total en Segundos de las llamadas: '))

print('Total por, ',cantidad_de_llamas,' llamadas, con una duracion de ',tiempo_total_de_llamadas,'segundos.\nEs de: $',(cantidad_de_llamas*costo_por_comunicacion)+(tiempo_total_de_llamadas*costo_por_segundos))
