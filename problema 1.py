def problema_1():
    pesos = float(input("Cantidad en pesos mexicanos: "))
    tipo_cambio = float(input("Precio de un dólar en pesos: "))
 
    dolar = pesos / tipo_cambio
    print(f"Con ${pesos:.2f} MXN puedes comprar ${dolar:.2f} USD")