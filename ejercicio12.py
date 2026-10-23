# Problema 12 - Ciclos: Realizar un algoritmo que pida N números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

# Pregunto cuantos numeros se van a ingresar (N)
N1 = int(input("Cuantos numeros vas a ingresar: "))

# Tres contadores, todos empiezan en 0
P = 0    # positivos (mayores que 0)
Ne = 0   # negativos (menores que 0)
Nu = 0   # nulos (iguales a 0)

# Se repite N veces
for i in range(N1):
    # Pido un numero
    N = int(input("Ingresa el numero: "))

    # Segun su valor, sumo al contador que le toca
    if N > 0:
        P += 1
    elif N < 0:
        Ne += 1
    else:
        Nu += 1

# Muestro los tres resultados
print(f"Positivos: {P}, Negativos: {Ne}, Iguales a 0: {Nu}")
