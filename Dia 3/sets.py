# un set puede declararse por su palabra reservada set([contenido]) o usando directamente los corchetes { }
# Es importante recalcar que en un set el contenido no debe ser repetido, sus elementos son inmutables

s1 = {1, 2, 3}

s1.add(5)
# remove y discard hacen lo mismo, la diferencia radica en que si intento eliminar un elemento inexistente
# remove arrojara un error, discard no arroja error, simplemente continua con la ejecucion normal
s1.remove(1)
s1.discard(8)
s1.pop()  # pop en este caso al no pasar ningun parametro y no haber un orden dentro de los sets
# eliminara un elemento completamente aleatorio

s1.clear()  # al dejar vacio vaciara completamente el set
print(s1)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s3 = s1.union(s2)
# print(s3)

# Cosas que se pueden usar en los sets
# mi_set = set([1, 2, 3, 4, 5])
#
# print(len(mi_set))
# print(2 in mi_set)
#

# mi_set = set([1, 2, (1, 2, 3), 4, 5])
# # dentro de un set no podra ser creado un diccionario ni una lista
# # sin embargo si acepta la creacion de un tuple
#
# print(type(mi_set))
# print(mi_set)

# print(mi_set)

# otro_set = {1, 2, 3}
# print(type(otro_set))
# print(otro_set)
