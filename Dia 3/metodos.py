texto = 'Este es el texto de fernando'
#replace toma un fragmento del texto y reemplaza por otro
resultado = texto.replace('fernando', 'todos')
#
print(resultado)
#find es igual que el metodo index, busca un determinado caracter dentro del string
#la diferencia entre ambos es que cuando buscas un caracter inexistente con find
#este no arroja un error, solo devuelve un -1
# resultado = texto.find('s')
#
# print(resultado)


# join es unir texto
# a = 'aprender'
# b = 'python'
# c = 'es'
# d = 'genial'
# e = ' '.join([a, b, c, d])  # toma los elementos en el array y los separa por lo que haya
# # en las comillas
# print(e)

# separar texto en elementos para guardar en una lista, si no pasamos parametros
# por defecto separa por espacios vacios
# resultado = texto.split('t')

# texto en minusculas
# resultado =  texto.lower()

# Pasar texto a mayusculas, tambien se puede usar con indices texto[3].upper()
# resultado =  texto.upper()
