frutas = {"manzana":1.20,"pera":1.75,"naranja":3.05}
fruta = frutas.get(input("Introduzca el nombre de la fruta cuyo precio quiere consultar: "))
print(fruta) if fruta is not None else print(f"No disponemos de esa fruta")