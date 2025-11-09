productos1 = {
    "manzana": 1.20,
    "naranja": 0.80,
    "plátano": 1.00,
    "pera": 1.50,
    "uva": 2.00
}

productos2 = {
    "naranja": 0.75,
    "plátano": 1.10,
    "sandía": 3.00,
    "melón": 2.50,
    "manzana": 1.25
}

productos_combinados = {}

for producto, precio in productos1.items():
    productos_combinados[producto] = precio

for producto, precio in productos2.items():
    if producto in productos_combinados:
        productos_combinados[producto] += precio
    else:
        productos_combinados[producto] = precio
print(productos_combinados)
    
