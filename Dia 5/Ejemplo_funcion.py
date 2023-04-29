precios_cafe = [('capuchino', 1.50), ('expresso',1.99), ('moka', 1.9)]

def cafe_mas_car(lista_precios):
    precio_mayor = 0
    cafe_mas_caro = ''

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe

    return (precio_mayor, cafe_mas_caro)

precio, cafe = cafe_mas_car(precios_cafe)

print(f'El café más caro es {cafe}, con un precio de {precio}')
