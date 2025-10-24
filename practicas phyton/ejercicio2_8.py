entrada = input("introduce una palabra o frase: ").replace(" ","")
entrada_2 = input("introduce otra palabra o frase: ").replace(" ","")

print("es un anagrama") if entrada == entrada_2 else print("no es un anagrama")