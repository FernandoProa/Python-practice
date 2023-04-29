def check_3_cifras(lista):
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False


resultado = check_3_cifras([55,99,600])

print(resultado)

# def check_3_cifras(numero):
#     return numero in range(100, 1000)
#
#
# resultado = check_3_cifras(69)
#
# print(resultado)
