def problema_10():
    can = int(input("Cantidad de lápices: "))
 
    if can >= 1000:
        pre = 0.85
    else:
        pre = 0.90
 
    tot = can * pre
    print(f"Precio por lápiz: ${pre:.2f}")
    print(f"Total a pagar: ${tot:.2f}")
 