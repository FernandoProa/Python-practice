nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        continue
    print(letra)
    #pasa a la siguiente iteración


# nombre = input("Tu nombre: ")
#
# for letra in nombre:
#     if letra == 'r':
#         break
#     print(letra)
    #break detiene la iteración actual

# respuesta = 's'
#
# while respuesta == 's':
#     pass
# pass literalmente no hace nada
#
# print('hola')


# respuesta = 's'
#
# while respuesta == 's':
#     respuesta = input("Quieres seguir? (s/n)")
# else:
#     print("gracias")

# monedas = 5
#
# while monedas > 0:
#     print(f"Tengo {monedas} monedas")
#     monedas -= 1
# else:
#     print("No tengo más dinero")
