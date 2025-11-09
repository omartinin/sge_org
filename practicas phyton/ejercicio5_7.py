from functools import reduce

texto = "Hola hola mundo mundo cruel"
texto = texto.lower().split(" ")

def contador(acu, x):
    acu[x] = acu.get(x,0)+1
    return acu

ocurrencias = reduce(contador, texto,{})

print(ocurrencias)

