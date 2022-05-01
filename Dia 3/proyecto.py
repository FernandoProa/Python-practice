cantLetras = 3
letras = []
texto = input('Ingresa un texto: ').lower()

for i in range(cantLetras):
    letras.append(input(f'Ingresa la letra # {i + 1}: ').lower())

for i in range(len(letras)):
    print(f'La cantidad de veces que aparece "{letras[i]}" en texto es de: {texto.count(letras[i])}')

print(f'La cantidad de letras que tiene el texto es de: {len(texto)}')

print(f'La primera letra del texto es: "{texto[0]}", y la ultima es: "{texto[len(texto) - 1]}" ')

print(f'Las palabras en el orden inverso quedarían: {texto[::-1]}')

if 'python' in texto:
    print('La palabra python aparece en el texto')
else:
    print('La palabra python no aparece en el texto')
