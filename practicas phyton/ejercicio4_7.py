empleados = {
    "Ana": 2500,
    "Carlos": 3200,
    "María": 2800,
    "Luis": 3000,
    "Sofía": 2700
}
for empleado, sueldo in empleados.items():
    if sueldo > 2800:
        print(empleado)
