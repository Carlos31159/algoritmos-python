# Problema 1 - Ciclos: Mostrar la tabla de multiplicar del numero 5.

print("Programa para tabla de multiplicar del numero 5")

# El ciclo se repite 10 veces: i vale 1, 2, 3 ... 10
for i in range(1, 11):
    # Multiplico 5 por el valor actual de i
    R = 5 * i
    # Muestro la operacion con su resultado
    print(f"5 X {i} = {R}")
