def problema_13():
    m = int(input("Duración de la llamada (minutos): "))
 
    t1 = min(m, 5)               # primeros 5 minutos
    t2 = min(max(m - 5, 0), 3)   # siguientes 3 minutos
    t3 = min(max(m - 8, 0), 2)   # siguientes 2 minutos
    t4 = max(m - 10, 0)          # el resto
 
    c1 = t1 * 1.00
    c2 = t2 * 0.80
    c3 = t3 * 0.70
    c4 = t4 * 0.50
    tot = c1 + c2 + c3 + c4
 
    print(f"Primeros 5 min   ({t1} min x $1.00): ${c1:.2f}")
    print(f"Siguientes 3 min ({t2} min x $0.80): ${c2:.2f}")
    print(f"Siguientes 2 min ({t3} min x $0.70): ${c3:.2f}")
    print(f"Resto de minutos ({t4} min x $0.50): ${c4:.2f}")
    print(f"Total a pagar: ${tot:.2f} MXN")