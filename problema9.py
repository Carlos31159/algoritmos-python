def problema_9():
    e1 = float(input("Calificación del examen 1: "))
    e2 = float(input("Calificación del examen 2: "))
    e3 = float(input("Calificación del examen 3: "))
 
    pro = e1 * 0.25 + e2 * 0.25 + e3 * 0.50
    print(f"El promedio del alumno es: {pro:.2f}")