# Problema 20 - Ciclos: Una compañía fabrica focos de colores (verdes, blancos y rojos). Se desea contabilizar, de un lote de N focos, el número de focos de cada color que hay en existencia.

# Pregunto cuantos focos tiene el lote (N)
N = int(input("¿Cuántos focos hay en el lote? "))

# Un contador por color, todos empiezan en 0
V = 0   # verdes
B = 0   # blancos
R = 0   # rojos

# Se repite una vez por foco
for i in range(1, N + 1):
    # Pido el color; strip quita espacios y upper lo pasa a mayuscula
    C = input(f"Color del foco {i} (V=verde, B=blanco, R=rojo): ").strip().upper()

    # Sumo al contador del color que escribio
    if C == "V":
        V += 1
    elif C == "B":
        B += 1
    elif C == "R":
        R += 1
    # Si escribio otra letra, no se cuenta
    else:
        print("  Color no válido, no se contabilizó.")

# Muestro cuantos focos hay de cada color
print("\n--- Existencias ---")
print(f"Verdes  (V): {V}")
print(f"Blancos (B): {B}")
print(f"Rojos   (R): {R}")
print(f"Total contabilizado: {V + B + R} de {N}")
