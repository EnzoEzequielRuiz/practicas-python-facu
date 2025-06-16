'''
Supongamos que una persona desea invertir su capital en un banco y quiere saber cuanto dinero tendra en su cuenta si el banco incrementa el 6% mensual (no acumulativo). Se le debe pedir al usuario el capital a invertir y la cantidad de meses. Por ejemplo, si invirte 500 mil pesos por 4 meses el banco deberia devolverle 620 mil pesos.
'''

monto_ingresar = float(input('Ingrese el monto: '))
interes_banco = 0.06
meses = int(input('Ingrese los meses que desea dejar su dinero: '))
intereses_ganados = (monto_ingresar * interes_banco) * meses

print('Su monto ingresado es de : $',monto_ingresar,' y los meses guardado ',meses,' meses\nInteres ganados: $',intereses_ganados,'\nTotal: $',monto_ingresar+intereses_ganados)