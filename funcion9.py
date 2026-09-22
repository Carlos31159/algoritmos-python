def obtener_s(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    else:
        return "Cero"

n = float(input("Ingresa un número: "))

print("El número es:", obtener_s(n))