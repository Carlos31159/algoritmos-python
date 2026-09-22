def m_d(a, b):
    if a >= b:
        return a
    else:
        return b

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("El mayor es:", m_d(a, b))