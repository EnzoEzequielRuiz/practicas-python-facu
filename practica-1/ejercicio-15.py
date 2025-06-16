'''
Un vendedor recibe un sueldo base de $42000 mas un 10% extra del total de sus ventas, el vendedor desea saber cuanto dinero obtendra en total en el mes si ha logrado realizar 3 ventas este mes. Tenga en cuenta el sueldo basico y la comision por las ventas.

Hacer un porgrama que solicite el monto de cada una de las ventas del mes e indique cual sera el sueldo final del vendedor. Por ejemplo, si realizo una venta de $12000, otra de $6000 y una tercera de $22000 su sueldo sera de $46000
'''

sueldo_base = 42000
comision_por_venta = .10

venta1 = 12000
venta2 = 6000
venta3 = 22000

print('--------------------------------------------------------------')
print('Su sueldo es: $',sueldo_base,'\nVentas realizadas 3:\nventa 1: $',venta1,'\nventa 2: $',venta2,'\nventa 3: $',venta3,'\nComisiones por venta 10%, mas sueldo: $',(venta1*comision_por_venta)+(venta2*comision_por_venta)+(venta3*comision_por_venta)+sueldo_base)
print('--------------------------------------------------------------')