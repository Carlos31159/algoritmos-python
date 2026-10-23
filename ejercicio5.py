# Problema 5 - Ciclos: Crea un programa que recorra los números del 1 al 20 e imprima únicamente aquellos que sean pares, indicando al final cuántos números pares se encontraron en total.

# c cuenta los numeros pares, empieza en 0
c = 0

# Recorro los numeros del 1 al 20
for i in range(1, 21):
    # Si al dividir entre 2 el residuo es 0, el numero es par
    if i % 2 == 0:
        # Lo imprimo
        print(i)
        # Y lo cuento
        c += 1

# Muestro cuantos pares hubo
print("Total de pares:", c)
