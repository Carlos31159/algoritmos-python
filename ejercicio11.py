# Problema 11 - Ciclos: Revisa en un ciclo el peso registrado de 10 maletas y cuenta cuántas superan el límite de 23 kg.

print("Peso de maletas")

# Su cuenta las maletas que pasan de 23 kg, empieza en 0
Su = 0

# Se repite 10 veces, una por maleta
for i in range(1, 11):
    # Pido el peso de la maleta
    N = int(input(f"Ingresa el peso de la maleta {i}: "))

    # Si pesa mas de 23, la cuento
    if N > 23:
        Su += 1

# Muestro cuantas maletas se pasaron
print(f"Cantidad de maletas que superaron el peso: {Su}")
