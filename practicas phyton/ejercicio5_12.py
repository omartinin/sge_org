lista1 = [1, 2]
lista2 = [3, 4]

def cartesiano(x):
    resultado = []
    for y in lista2:
        resultado.append((x,y))
    return resultado
producto_cartesiano = list(map(cartesiano, lista1))
producto_cartesiano = sum(producto_cartesiano, [])

print(producto_cartesiano)