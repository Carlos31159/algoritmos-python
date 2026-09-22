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
 
 
# Repaso 12: banquetes "La langosta ahumada"
def problema_12():
    per = int(input("Número de personas: "))
 
    if per > 300:
        cp = 75.00
    elif per > 200:  # más de 200 y hasta 300
        cp = 85.00
    else:
        cp = 95.00
 
    pres = per * cp
    print(f"Costo por platillo: ${cp:.2f}")
    print(f"Presupuesto total: ${pres:.2f}")