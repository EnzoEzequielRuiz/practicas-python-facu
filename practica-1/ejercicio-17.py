'''
La empresa que administra los cajeros automaticos lo contrata para que programen la entrega de billetes, el usuario ingresa la cantidad de dinero que desea y usted debe indicar cuantos billetes de cada demonimacion debe entregar.
Es importante entregar siempre la menor cantidad de billetes.
'''

cajero_automatico = int(input('Ingrese la cantidad de dinero que desee retirar: '))

billete_20mil = cajero_automatico // 20000
resto_20mil = cajero_automatico % 20000

billete_10mil = resto_20mil // 10000
resto_10mil = resto_20mil % 10000

billete_2mil = resto_10mil // 2000
resto_2mil = resto_10mil % 2000

billete_mil = resto_2mil // 1000
resto_mil = resto_2mil % 1000

billete_500 = resto_mil // 500
resto_500 = resto_mil % 500

billete_200 = resto_500 // 200
resto_200 = resto_500 % 200

billete_100 = resto_200 // 100
resto_100 = resto_200 % 100

print('Restirado: $',cajero_automatico,'\nSon,',billete_20mil,'billetes de $20.000 pesos\nSon,',billete_10mil,'billetes de $10.000 pesos\nSon,',billete_2mil,'billetes de $2.000 pesos\nSon,',billete_mil,'billetes de $1.000 pesos\nSon,',billete_500,'billetes de $500 pesos\nSon,',billete_200,'billetes de $200 pesos\nSon,',billete_100,'billetes de $100 pesos.' )