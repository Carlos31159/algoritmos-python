# Problema 10 - Ciclos: Una discoteca tiene 8 personas registradas. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).

print("Entrada Discoteca")

# Su cuenta a los menores de edad, empieza en 0
Su = 0

# Se repite 8 veces, una por persona
for i in range(1, 9):
    # Pido la edad
    N = int(input("Ingresa tu edad: "))

    # Si tiene 18 o mas, es mayor de edad
    if N >= 18:
        print("Pasas, eres mayor de edad")
    # Si no, es menor: lo aviso y lo sumo al contador
    else:
        print("Eres menor de edad, pasa bajo supervision")
        Su += 1

# Muestro cuantos menores hay
print(f"Cantidad de menores de edad ingresados: {Su}")
