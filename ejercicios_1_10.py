#1

""" def calcular_propina():

    total = int(input("Ingrese el valor total de la cuenta aquí: "))

    if total >= 100000:
        propina = 0.15
    else:
        propina = 0.10

    cuenta = total + (total * propina)
    print(f"Su cuenta tendrá el valor de ${cuenta:.0f}.") """

#2

""" def repeticiones():

    n = int(input("Ingrese aquí el número de repeticiones: "))

    if n % 2 != 0:
        print("Mantén el ritmo.")
    else:
        print("Excelente forma")

repeticiones() """

#3

""" def aplicar_descuentos():

    total = 0

    while True:

        precio = float(input("Ingrese el precio (0 para finalizar): "))

        if precio == 0:
            break

        
        if precio > 50000:
            precio *= 0.90  

        total += precio

    print(f"El total de sus compras con descuento es: ${total:.0f}") """

#4

""" def evaluar_credito():

    ingresos = int(input("Ingrese sus ingresos aquí: "))
    edad = int(input("Ingrese su edad aquí: "))

    if ingresos > 2000000 and 25 <= edad <= 60:
        print("Credito aprobado.")
    else:
        print("Credito rechazado.")

evaluar_credito() """

#5

""" def promedio_notas():

    while True:

        print("\n--- Nuevo estudiante ---")
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 3.0:
            print(f"Promedio: {promedio:.2f}, Aprobado ")
        else:
            print(f"Promedio: {promedio:.2f},  Reprobado ")

        continuar = input("\n¿Desea ingresar otro estudiante? (s/n): ").lower()
        if continuar != "s":
            print("Fin del registro de notas.")
            break

promedio_notas() """

#6

""" def simular_viaje():

    pasajeros = 0

    while pasajeros < 10:
        nuevos = int(input("¿Cuántos pasajeros suben? "))
        
        for i in range(nuevos):
            pasajeros += 1

            if pasajeros > 10:
                print("Bus lleno ")
                return
            print(f"Pasajero {pasajeros} a bordo.")

simular_viaje() """

#7

""" def hornear_pan():
    
    lote = int(input("Número de lotes: "))

    for lote in range(1, lote + 1):
        print(f"Horneando lote {lote}")

        if lote % 3 == 0:
            print("Verificación de calidad.")
    
    print("Producción terminada.")

hornear_pan() """

#8

""" def calcular_entradas():

    total = 0

    while True:

        edades = int(input("Ingrese la edad del cliente (0 para aplicar precio): "))

        if edades == 0:
            break
        if edades >= 60:
            precio = 4000
        elif 12 <= edades <= 59:
            precio = 8000
        else:
            precio = 5000
        
        total += precio
        print(f"El precio sera de ${precio:.0f}.")

    print(f"\nTotal a pagar por todas las entradas: ${total}")

calcular_entradas() """

#9

""" def calcular_puntos():

    total = 0

    compras = int(input("Ingrese la cantidad de compras: "))

    for compra in range(1, compras + 1):
            
        if compra % 3 == 0:
            total += 10
        else:
                total += 5
            
    print(f"Su cantidad de puntos totales es de {total} puntos.")

calcular_puntos() """

# 10

""" def tabla_multiplicar():

    n = int(input("Ingrese el número: "))

    for i in range(1, 11):
        
        tabla = i * n
        print(f"{i} x {n} = {tabla}.")

        if tabla > 50:
            print("Resultado alto.")

tabla_multiplicar() """




