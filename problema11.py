def problema_11():
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    c = float(input("Tercer número: "))
 
    if a >= b and a >= c:
        may = a
    elif b >= a and b >= c:
        may = b
    else:
        may = c
 
    print(f"El mayor es: {may}")
 
