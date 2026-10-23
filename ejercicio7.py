# Problema 7 - Ciclos: Un sensor en la puerta de una discoteca registra la edad de 8 personas que intentan entrar. Usa un contador para determinar cuántas personas son menores de edad (menores a 18 años).

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
    # Si no, es menor de edad y lo sumo al contador
    else:
        print("No pasas, menor de edad")
        Su += 1

# Muestro cuantos menores intentaron entrar
print(f"Cantidad de menores de edad: {Su}")
