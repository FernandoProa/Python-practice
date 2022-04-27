#las listas en python pueden contener una mezcla de distintos tipos de datos
# mi_lista = ['a','b','c']
# mi_lista2 = ['d','e','f']
# mi_lista3 = mi_lista + mi_lista2

#ordenar una lista, sirve para letras o numeros
#sort ordena y no devuelve nada, por lo que no puede asignarse a otra variable
# new_list = lista.sort() -> no se puede realizar
lista = ['g','o','b','m','c']
lista.sort()
#inversion del orden, lo ultimo lo pone primero
lista.reverse()
print(lista)



#Agregar elementos
# mi_lista3.append('g')
#eliminar elementos, si lo dejas sin parametros, elimina el ultimo de los elementos
#a no ser que especifiques el indice a eliminar
# mi_lista3.pop()
#el elemento eliminado se puede almacenar en otra variable
# eliminado =mi_lista3.pop()
#
# print(mi_lista3)
# print(eliminado)

#se pueden sobreescribir cualquiera de sus elementos
# mi_lista3[0] = 'alfa'




# resultado = len(mi_lista)
#toma un solo indice de la lista
# resultado = mi_lista[0]
#toma un rango de indices -1, 0 hasta 2, pero no incluye el 2
# resultado = mi_lista[0:2]
#se pueden concatenar las listas
# print(mi_lista + mi_lista2)


# resultado = mi_lista[0:2]
# otra_lista = ['hola', 55, 6.1]
# print(resultado)