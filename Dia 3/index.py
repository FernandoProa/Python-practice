mi_texto = 'Esta es una prueba'
#Pueden usarse tambien indices negativos
# resultado = mi_texto[-4]
#para buscar dentro del texto, ya sean letras o palabras, es sensible a mayusculas
# resultado = mi_texto.index('prueba')
# Adicional se pueden pasar 2 parametros opcionales start y end, desde donde busca hasta donde
# resultado = mi_texto.index('a', 3, 10)
# Metodo rindex busca de derecha a izquierda (al reves)

# resultado = mi_texto.rindex('a', 3, 10)
resultado = mi_texto.rindex('a')

print(resultado)