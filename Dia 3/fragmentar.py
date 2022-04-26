texto = 'ABCDEFGHIJKLM'
#index string[index:hasta] -> el hasta no incluye ese numero, por ejemplo string[2:5] desde el 2 hasta
#el 5 pero sin incluir este numero (5), si se omite y solo dejan 2 puntos [2:] se interpreta como
#desde el 2 y hasta el final, misma logica dejando el primero vacio [:5] inicio hasta 5
#el tercero es cada cuantos caracteres se va tomando
fragmento = texto[2:10:2]
# Si el tercer factor se pone -1 la cadena se invierte completamente
# fragmento = texto[::-1]

print(fragmento)