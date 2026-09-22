def problema_7():
    pre = float(input("Precio del artículo: $"))
 
    pd = pre - pre * 0.20
    pf = pd + pd * 0.15
 
    print(f"Precio con descuento: ${pd:.2f}")
    print(f"Precio final (con IVA): ${pf:.2f}")
 
 
def problema_7_menu():
    print("1. Laptop      - $12000.00")
    print("2. Audífonos   - $800.00")
    op = input("Elige un producto (1 o 2): ")
 
    if op == "1":
        nom, pre = "Laptop", 12000.00
    elif op == "2":
        nom, pre = "Audífonos", 800.00
    else:
        print("Opción no válida")
        return
 
    pd = pre - pre * 0.20
    pf = pd + pd * 0.15
 
    print(f"Producto: {nom}")
    print(f"Precio: ${pre:.2f}")
    print(f"Precio con descuento (20%): ${pd:.2f}")
    print(f"Precio final (IVA 15%): ${pf:.2f}")