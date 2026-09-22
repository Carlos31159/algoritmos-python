def problema_8():
    pre = float(input("Precio del traje: $"))
 
    if pre > 2500:
        por = 0.15
    else:
        por = 0.08
 
    des = pre * por
    pf = pre - des
 
    print(f"Descuento: ${des:.2f}")
    print(f"Precio final a pagar: ${pf:.2f}")
 
 
# Tarea 1: viaje de estudios
def tarea_1():
    al = int(input("Número de alumnos: "))
 
    if al <= 0:
        print("El número de alumnos debe ser mayor a 0")
        return
 
    if al >= 100:
        ca = 65.00
        tc = ca * al
    elif al >= 50:
        ca = 70.00
        tc = ca * al
    elif al >= 30:
        ca = 95.00
        tc = ca * al
    else:
        tc = 4000.00  # renta fija del autobús
        ca = tc / al
 
    print(f"Cobro por alumno: ${ca:.2f}")
    print(f"Pago a la compañía de viajes: ${tc:.2f}")