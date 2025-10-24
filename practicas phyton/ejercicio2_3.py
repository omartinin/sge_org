str = input("Dime un palíndromo: ").replace(" ","")

print("es palíndromo" if str == str[::-1] else "no es palíndromo")
