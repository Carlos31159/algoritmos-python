# Problema 18 - Ciclos: Una empresa tiene el registro de las horas que trabaja diariamente un empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el sueldo que recibirá por las horas trabajadas

print("Programa para calcular cuanto ganas a la semana")

# Pido cuanto le pagan por hora
N2 = int(input("Ingresa cuanto te pagan la hora: "))

# H guarda el total de horas, empieza en 0
H = 0

# Se repite 6 veces, una por dia
for i in range(1, 7):
    # Pido las horas trabajadas ese dia
    N1 = int(input(f"Ingresa cuantas horas trabajaste el dia {i}: "))
    # Las sumo al total de horas
    H += N1

# Sueldo = total de horas por lo que pagan cada hora
Su = H * N2

# Muestro el total de horas y el sueldo
print(f"Horas trabajadas: {H}")
print(f"Sueldo a recibir por tus {H} horas trabajadas: {Su}")
