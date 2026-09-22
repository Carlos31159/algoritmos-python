def problema_14():
    m = int(input("Duración de la llamada (minutos): "))
    print("1. Domingo")
    print("2. Día hábil")
    d = input("Elige el tipo de día (1 o 2): ")
 
    if d == "1":
        por = 0.03
    elif d == "2":
        print("1. Matutino")
        print("2. Vespertino")
        tu = input("Elige el turno (1 o 2): ")
        if tu == "1":
            por = 0.15
        elif tu == "2":
            por = 0.10
        else:
            print("Turno no válido")
            return
    else:
        print("Opción no válida")
        return
 
    t1 = min(m, 5)
    t2 = min(max(m - 5, 0), 3)
    t3 = min(max(m - 8, 0), 2)
    t4 = max(m - 10, 0)
 
    c1 = t1 * 1.00
    c2 = t2 * 0.80
    c3 = t3 * 0.70
    c4 = t4 * 0.50
    sub = c1 + c2 + c3 + c4
 
    imp = sub * por
    tot = sub + imp
 
    print(f"Primeros 5 min   ({t1} min x $1.00): ${c1:.2f}")
    print(f"Siguientes 3 min ({t2} min x $0.80): ${c2:.2f}")
    print(f"Siguientes 2 min ({t3} min x $0.70): ${c3:.2f}")
    print(f"Resto de minutos ({t4} min x $0.50): ${c4:.2f}")
    print(f"Subtotal: ${sub:.2f}")
    print(f"Impuesto ({por * 100:.0f}%): ${imp:.2f}")
    print(f"Total a pagar: ${tot:.2f} MXN")