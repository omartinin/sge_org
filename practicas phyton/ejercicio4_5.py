productos = {
    "Electrónica": "Smartwatch",
    "Hogar": "Cafetera",
    "Ropa": "Bufanda",
    "Deportes": "Cuerda de saltar",
    "Juguetes": "Coche de juguete",
}

productos_keyvalued = {valor : clave for clave, valor in productos.items()}

print(productos_keyvalued)