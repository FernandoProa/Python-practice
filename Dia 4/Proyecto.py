# Crear un juego que pregunte al usuario el nombre, una cadena de texto que indique que adivine un numero del 1 al 100 con un total de 8 intentos
# Debe ser un numero entre 1 y 100 el que el usuario ingrese
from random import *

numero = randint(1, 100)
intentos = 8
nombre = input("Ingresa tu nombre: ")
respuesta = 0

print(
    f"{nombre}, he pensado en 1 número entre el 1 y el 100, dispones de 8 intentos para adividar dicho número, ¿Cuál crees que es el número?")
while intentos > 0:
    respuesta = int(input("Ingresa un número entre 1 y 100: "))
    if respuesta not in range(1, 101):
        print("Debes escoger un número entre el 1 y el 100, vuelve a intentarlo")
        continue

    if respuesta < numero:
        intentos -= 1
        print(
            f"El número ingresado es menor al numero que he pensado, inténtalo nuevamente. Tienes {intentos} intentos más")
    elif respuesta > numero:
        intentos -= 1
        print(f"El número ingresado es mayor al núm que he pensado, inténtalo nuevamente. Tienes {intentos} más")
    elif respuesta == numero:
        print(f"Has adivinado el número, te ha tomado {8 - intentos} intentos")
        break

if respuesta != numero:
    print(f"Lo siento, se han agotado los intentos. El número era: {numero}")
