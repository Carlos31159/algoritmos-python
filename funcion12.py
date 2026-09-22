def CAL(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    else:
        return "F"

n = float(input("Ingresa la calificación: "))

print("Calificación:", CAL(n))