'''
Escribir en Python un programa que pida al usuario que ingrese dos valores y los guarde en dos variables, "X" e "Y". El programa debera intercambiar los valores de "X" e "Y" y luego mostrar en pantalla:

El valor de x es: <x>
El valor de y es: <y>
'''
print('---------------------------------------------------')
print('Intercambiar valores')
x = int(input('Ingrese el valor de x: '))
y = int(input('Ingrese el valor de y: '))
guarda = x
x = y
y = guarda
print('El valor de x es:',x,'\nEl valor de y es:',y)