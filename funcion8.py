def a_t(b, h):
    if b > 0 and h > 0:
        return (b * h) / 2
    else:
        return 0

b = float(input("Ingresa la base: "))
h = float(input("Ingresa la altura: "))

print("Área:", a_t(b, h))