# Problema 4 - Ciclos: Pide al usuario que ingrese N números enteros enteros uno por uno. Al finalizar la lectura, muestra la suma total de todos los números ingresados.

# Pregunto cuantos numeros se van a sumar (N)
N1 = int(input("Cuantos numeros a sumar vas a ingresar: "))

# Su guarda la suma, empieza en 0
Su = 0

# Se repite N veces
for i in range(N1):
    # Pido un numero
    N = int(input("Ingresa el numero: "))
    # Lo sumo al total
    Su += N

# Al terminar el ciclo muestro la suma
print(f"La suma total de tus numeros es: {Su}")
