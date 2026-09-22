def operacion_b(a, b, op):
    if op == "suma":
        return a + b
    elif op == "resta":
        return a - b
    elif op == "multiplica":
        return a * b
    else:
        return "Operación no válida"

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
op = input("Escribe suma, resta o multiplica: ")

print("Resultado:", operacion_b(a, b, op))