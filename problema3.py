def problema_3():
    h = float(input("Tiempo que estuvo el auto (en horas, ej. 2.3): "))
    t = float(input("Costo por hora: $"))
 
    hc = math.ceil(h)  # 2.3 horas -> 3 horas
    c = hc * t
    print(f"Horas a cobrar: {hc}")
    print(f"Total a pagar: ${c:.2f}")