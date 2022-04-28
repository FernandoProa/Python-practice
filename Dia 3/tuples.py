# los tuples ocupan menos espacio en memoria en comparacion de las Listas
# no se pueden modificar como tal

t = (1, 2, 3, 1)
print(t.count(1))  # count permite contar la cantidad de apariciones de un valor dentro del tuple
print(t.index(1))  # count permite consultar el indice del valor que estamos pasando

# t = (1, 2, 3)

# x, y, z = t  # podemos asignar los valores de esta manera siempre y cuando declaremos la misma cantidad
# de variables y hayan los mismos elementos

# print(x, y, z)

#
# mi_tuple = (1, 2, 3, 4)
# mi_tuple = list(mi_tuple)  # para sobreescribir se debe guardar en una lista
# mi_tuple = tuple(mi_tuple)  # se vuelve a pasar a tuple
# # mi_tuple2 = (1, 2, (10, 20), 4)  # se puede almacenar un tuple dentro de otro
# # t = (5, 5.6, 'string') pueden almacenar diferentes tipos de datos
#
# # print(mi_tuple2[2][0]) # para acceder a un tuple dentro de otro
# print(mi_tuple)
