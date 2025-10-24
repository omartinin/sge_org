codigo_rle = "2a3b2 4s"
contador = 1
n = 0
resultado = ""
for c in codigo_rle:
    if (contador % 2 == 0):
        resultado += c*n
    else:
        n = int(c)
    contador += 1

print(resultado)
    
