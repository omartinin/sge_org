palabras = ["sol", "luna", "estrella", "cielo", "mar"]

d_palabras = {}
list(map(lambda x: d_palabras.setdefault(len(x),[]).append(x),palabras))

print(d_palabras)