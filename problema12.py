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