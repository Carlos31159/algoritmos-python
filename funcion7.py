def E_M(e):
    if e >= 18:
        return "Mayor"
    else:
        return "Menor"

e = int(input("Ingresa tu edad: "))

print(E_M(e))