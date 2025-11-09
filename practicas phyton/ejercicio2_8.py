entrada = list(input("introduce una palabra o frase: ").replace(" ","").lower()).sort()
entrada_2 = list(input("introduce otra palabra o frase: ").replace(" ","").lower()).sort()

print("es un anagrama") if entrada == entrada_2 else print("no es un anagrama")