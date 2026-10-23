# Problema 16 - Ciclos: Un empleado de la tienda “Tiki Taka” realiza N ventas durante el día, se requiere saber cuántas de ellas fueron mayores a $1000, cuántas fueron mayores a $500 pero menores o iguales a $1000, y cuántas fueron menores o iguales a $500. Además, se requiere saber el monto de lo vendido en cada categoría y de forma global. Realice un algoritmo que permita determinar lo anterior

# Pregunto cuantas ventas hubo (N)
N1 = int(input("Cantidad de ventas realizadas: "))

# Contadores de ventas por categoria, empiezan en 0
P = 0    # ventas mayores a 1000
Ne = 0   # ventas mayores a 500 y menores o iguales a 1000
Nu = 0   # ventas menores o iguales a 500

# Acumuladores del dinero vendido por categoria, empiezan en 0
SP = 0
SNe = 0
SNu = 0

# Se repite una vez por venta
for i in range(1, N1 + 1):
    # Pido el monto de la venta
    N = int(input(f"Ingresa el monto de la venta {i}: "))

    # Segun el monto, cuento la venta y sumo el dinero a su categoria
    if N > 1000:
        P += 1
        SP += N
    elif N > 500:
        Ne += 1
        SNe += N
    else:
        Nu += 1
        SNu += N

# El total global es la suma de las tres categorias
Total = SP + SNe + SNu

# Muestro los resultados
print(f"Ventas mayores a 1000: {P} (monto: ${SP})")
print(f"Ventas mayores a 500 y hasta 1000: {Ne} (monto: ${SNe})")
print(f"Ventas menores o iguales a 500: {Nu} (monto: ${SNu})")
print(f"Monto total vendido: ${Total}")
