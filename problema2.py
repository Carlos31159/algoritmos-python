def problema_2():
    an = int(input("Año en que naciste: "))
    aa = date.today().year
 
    E = aa - an
    print(f"La edad del solicitante es: {E} años")