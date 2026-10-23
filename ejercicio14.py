# Problema 14 - Ciclos: Se requiere un algoritmo para determinar, de N cantidades, cuántas son menores o iguales a cero y cuántas mayores a cero

# Pregunto cuantas cantidades se van a ingresar (N)
N1 = int(input("Cuantas cantidades vas a ingresar: "))

# Dos contadores, ambos empiezan en 0
P = 0    # mayores a cero
Nu = 0   # menores o iguales a cero

# Se repite N veces
for i in range(N1):
    # Pido una cantidad
    N = int(input("Ingresa la cantidad: "))

    # Si es mayor a 0 sumo a P, si no (0 o negativo) sumo a Nu
    if N > 0:
        P += 1
    else:
        Nu += 1

# Muestro los dos resultados
print(f"Mayores a cero: {P}, Menores o iguales a cero: {Nu}")
