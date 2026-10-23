# Problema 13 - Ciclos: Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere saber cuánto lleva ahorrado cada mes.

print("Ahorro anual")

# Su guarda lo ahorrado hasta el momento, empieza en 0
Su = 0

# Se repite 12 veces, una por mes
for i in range(1, 13):
    # Pido cuanto se deposita este mes
    N = int(input(f"Cuanto ahorraras el mes {i}: "))
    # Lo sumo a lo que ya llevaba
    Su += N
    # Muestro cuanto lleva ahorrado hasta este mes
    print(f"Cantidad guardada hasta el mes {i}: {Su}")

# Al final muestro el total del año
print(f"Cantidad total guardada en el año: {Su}")
