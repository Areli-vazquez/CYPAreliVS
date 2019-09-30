MAT = int(input("Ingresa tu matícula:"))
CAL1 = float(input("Ingresa tu primera calificación:"))
CAL2 = float(input("Ingresa tu segunda calificación:"))
CAL3 = float(input("Ingresa tu tercera calificación:"))
CAL4 = float(input("Ingresa tu cuarta calificación:"))
CAL5 = float(input("Ingresa tu quinta calificación:"))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5)/5
if PRO >= 6:
    print(f"La matrícula: {MAT}, tiene el promedio de: {PRO}")
    print(f"ALUMNO APROBADO")
else: 
    print(f"La matrícula: {MAT}, tiene el promedio de: {PRO}")
    print(f"ALUMNO NO APROBADO")
print("Fin del programa")
