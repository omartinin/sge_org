#print("Hola mundo")

#saludar = True
#if (saludar):
#    nombre = "Omar"
#    print("Hola " + nombre)
#print("Adios")

num = input("Dime un número: ")
if (not num.isdigit()):
    print("No es un número.")
elif (int(num) % 2 == 0 ):
    print(num + " es par.")
else:
    print(num + " es impar.")

edad = input("Dime tu edad: ")
msg = (
    "no es un número" if not edad.isdigit() else
    "Eres mayor de edad" if int(edad) >= 18 else
    "Eres menor de edad"
    )
print (msg)

ciclo = input("Qué ciclo estás estudiando?")

msg = (
    "Desarrollo de aplicaciones multiplataforma" if ciclo == "DAM" else
    "Administración de sistemas informáticos en red" if ciclo == "ASIR" else
    "Desarrollo de aplicaciones web" if ciclo == "DAW" else "No conozco ese ciclo"
    )
print (msg)

for cf in ["DAM","DAW", "ASIR"]:
    print(ciclo)

for a in range(3): #itera desde 0 hasta 3
    print(a)

for b in range(2, 4): #itera desde 2 hasta 4
    print(b)

for c in range(1,9,3): #itera del 1 al 9 saltando de 3 en 3
    print(c)

a = 1
while (a < 4):
    a+=1
    print(a)
else:
    print("Hemos llegado al 4")

a = input("Qué ciclo estudias?")
match a: # switch de java
    case "DAM" | "DAW":
        print("Es un ciclo de desarrollo")
    case "ASIR":
        print("Administración de sistemas informáticos en red")
    case _: # default de java
        print("No lo conozco")

import sys
x = 5**10000 # 5 elevado a 10000
y = 10
print(sys.getsizeof(x), type(x)) # devuelve el tamaño en memoria de x
print(sys.getsizeof(y), type(y))

print(0o1234) #0o octal
print(0x1AF5) #0x hexadecimal
print(0b1010) #0b binario
int("0xAB", 16) # el numero y la base. lo pasa a int
bool(10) # da verdadero cualquier numero, cadena, array... que no sea 0 o este vacia.

numero = input("introduzca un número")

while (not numero.isdigit()):

    numero = input("introduzca un número")

