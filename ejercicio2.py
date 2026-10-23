# Problema 2 - Ciclos: Mostrar la tabla de multiplicar de un n numero ingresado por teclado.

# Pido el numero del que quiero la tabla
N = int(input("Numero que quieres la tabla de multiplicar: "))

# El ciclo se repite 10 veces: i vale 1, 2, 3 ... 10
for i in range(1, 11):
    # Multiplico el numero ingresado por i
    R = N * i
    # Muestro la operacion con su resultado
    print(f"{N} X {i} = {R}")
