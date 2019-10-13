TIPOENF = int(input("Ingrese el tipo de enfermedad que tiene el paciente(1-4):"))
NOM = str(input("Ingrese el nombre del paciente:"))
EDAD = int(input("Ingresa la edad del paciente:"))
DIAS = int(input("Ingresa el número de días que estuvo hospitalizado el paciente:"))
if TIPOENF == 1:
    COSTOT = DIAS * 25 
    if EDAD >=14:
        if EDAD <=22:
            COSTOT = COSTOT * 1.10
            print(f"El paciente {NOM} tiene que pagar ${COSTOT} por {DIAS} días.")
        else: 
            print(f"El costo total es: ${COSTOT}")
     
if TIPOENF == 2:
    COSTOT = DIAS * 16
    if EDAD >=14:
        if EDAD <=22:
            COSTOT = COSTOT * 1.10
            print(f"El paciente {NOM} tiene que pagar ${COSTOT} por {DIAS} días.")
        else:
            print(f"El costo total es: ${COSTOT}")

if TIPOENF == 3:
    COSTOT = DIAS * 20
    if EDAD >=14:
        if EDAD <=22:
            COSTOT = COSTOT * 1.10
            print(f"El paciente {NOM} tiene que pagar ${COSTOT} por {DIAS} días.")
        else:
            print(f"El costo total es: ${COSTOT}")

if TIPOENF == 4:
    COSTOT = DIAS * 32
    if EDAD >=14:
        if EDAD <=22:
            COSTOT = COSTOT * 1.10
            print(f"El paciente {NOM} tiene que pagar ${COSTOT} por {DIAS} días.")
        else:
            print(f"El costo total es: ${COSTOT}")
print("FIND EL PROGRAMA")
