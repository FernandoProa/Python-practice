nombre = input('Dime tu nombre: ')
ventas = float(input('Ingresa el total de las ventas realizadas: '))

comision = round((ventas * 13) / 100, 4)

print(f'Ok {nombre}, tu comisión por ventas será de: {comision}')
# print(ventas)
