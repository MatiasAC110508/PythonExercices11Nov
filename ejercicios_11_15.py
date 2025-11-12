#11

""" def calcular_millas():
    
    viajes = 0
    millas = 0
    
    while True:
        
        km = input('Ingrese los kilometros recorridas en su viaje\n("fin" para mostrar el acumulado): ').strip().lower()
        
        if km == "fin":
            break
        if float(km) < 1000:
            viajes += 1
            millas += 500
        elif 1000 <= float(km) <= 3000:
            viajes += 1
            millas += 1000
        else:
            viajes += 1
            millas += 2000
        
    print(f"La suma de tus {viajes} viajes dan como resultado {millas} millas.")
    
calcular_millas() """
        
#12

""" def evaluar_paciente():
    
   print("--Bienvenido al ESV (0 para salir.)--\n")
   
   while True:
        
        fc = int(input("Ingrese la FC: "))
        
        if fc == 0:
            break
        
        temp = int(input("Ingrese la temp: "))
        
        if temp == 0:
            break
        
        if fc > 100 or temp > 38:
            print("\nPaciente en observación.")
        else:
            print("\nPaciente fuera de observación.")
            
evaluar_paciente() """

#13

""" def carrito():
    
    total = 0
    
    while True:
        
        p = int(input("Ingrese el precio de su producto (0 para finalizar): "))
        
        if p == 0:
            print(f"El total de sus productos es de ${total:.0f}.")
            break
        
        if p < 0:
            print("ERROR: Porfavor ingrese otro valor.\n")
            continue
        elif p > 100000:
            total += p * 0.80
            print("Obtuviste un descuento sobre tu producto del 20%.\n")
        else:
            total += p
            print("Producto agregado exitosamente.\n")
            
carrito() """

#14

""" def calcular_factorial():
    
    resultado = 1
     
    f = int(input("Ingrese su n!= "))
        
    for n in range(1, f + 1):
            
        resultado *= n
    
    print(f"{f}! = {resultado}.")

            
calcular_factorial() """

#15

""" def evaluar_empleado():
    
    name = input("Ingresa el nombre: ")
    horas = int(input("Ingresa las horas: "))
    h_l = 0
    h_e = 0
    
    for h in range(1, horas + 1):
        if h > 8:
            h_e += 1
            print(f"\n{h} es una hora extra laboral.")
        else:
            h_l += 1
            print(f"\n{h} es una hora laboral.")
    
    print(f"\nEl total de las horas trabajadas\npor el empleado {name} es de {h_l + h_e}.")
    
evaluar_empleado() """
    
            
            
    
    

         