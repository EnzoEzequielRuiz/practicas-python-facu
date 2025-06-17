'''
Escribir en Python un programa que pida al usuario que ingrese tres valores y los guarde en tres variables, x,y,z.
El programa debera intercambiar circularmente los valores de x,y,z, es decir, x debe tomar el valor de y, y el valor de z y z el valor de x. Y luego mostrarlos en pantalla:

El valor de x es: <x>
El valor de y es: <y>
El valor de z es: <z>
'''


x = int(input('Ingrese el valor de x:'))
y = int(input('Ingrese el valor de y:'))
z = int(input('Ingrese el valor de z:'))

guarda1 = z
guarda2 = y

z = x
x = guarda2
y = guarda1

print('---------------------------------------------------')
print('El valor de x es:',x,'\nEl valor de y es:',y,'\nEl valor de z es:',z)
print('---------------------------------------------------')