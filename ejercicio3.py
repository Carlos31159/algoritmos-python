# Problema 3 - Ciclos: Pide al usuario que ingrese 5 números enteros uno por uno. Al finalizar la lectura, muestra la suma total de todos los números ingresados.

print("5 numeros a sumar")

# Su guarda la suma, empieza en 0
Su = 0

# Se repite 5 veces, una por cada numero
for i in range(1, 6):
    # Pido un numero
    N = int(input("Ingresa el numero: "))
    # Lo sumo al total
    Su += N

# Al terminar el ciclo muestro la suma
print(f"La suma total de tus numeros es: {Su}")
