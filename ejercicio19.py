# Problema 19 - Ciclos: Un profesor tiene un salario inicial de $1500, y recibe un incremento de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6 años? ¿Qué salario ha recibido en cada uno de los 6 años? Realice el algoritmo

print("Salario de un maestro con incremento anual durante 6 años")

# Ma es el salario actual, empieza en 1500
Ma = 1500

# Se repite 6 veces, una por año
for i in range(1, 7):
    # Calculo el 10% de aumento
    R2 = Ma * 0.10
    # Nuevo salario = salario actual + aumento
    R3 = round(Ma + R2, 2)   # redondeo a 2 decimales
    # Muestro el salario de este año
    print(f"Sueldo a recibir en el año {i}: {R3}")
    # El nuevo salario es el actual para el siguiente año
    Ma = R3

# Al salir del ciclo, Ma tiene el salario del ultimo año
print(f"Salario al cabo de 6 años: {Ma}")
