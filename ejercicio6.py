# Problema 6 - Ciclos: Diseñe una aplicación que permita ingresar n números y muestre y sume los números pares.

# Pregunto cuantos numeros se van a ingresar
n = int(input("Cuantos numeros ingresaras? "))

# s guarda la suma de los pares, empieza en 0
s = 0

# Se repite n veces
for i in range(n):
    # Pido un numero
    x = int(input("Ingresa un numero: "))

    # Si el residuo entre 2 es 0, es par
    if x % 2 == 0:
        # Lo muestro
        print("Par:", x)
        # Lo sumo a los pares
        s += x

# Muestro la suma de todos los pares
print("Suma de pares:", s)
