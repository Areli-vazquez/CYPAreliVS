NOM = str(input("Escribe tu nombre completo:"))
MAT = int(input("Escribe tu matricula de alumno:"))
CARR = str(input("El alumno está inscrito en la carrera de:"))
SEM = int(input("El alumno está cursando el semestre:"))
PROM = float(input("El alumno tiene un promedio de:"))
if CARR =="Economia":
    SEM >=6
    if PROM >=8.8:
        print(f"El alumno {NOM} con la matrícula {MAT} de la carrera de {CARR} a sido ACEPTADO")
    else:
        print(f"El alumno {NOM} con la matrícula {MAT} de la carrera de {CARR} no a sido ACEPTADO")
        
elif CARR =="Computación":
    SEM >6 
    if PROM >=8.5:
        print(f"El alumno {NOM} con la matrícula {MAT} de la carrera de {CARR} a sido ACEPTADO")
    else:
        print(f"El alumno {NOM}  no a sido ACEPTADO")
        
elif CARR =="Contabilidad": 
        SEM > 5
        if PROM >= 8.5:
             print(f"El alumno {NOM} con la matrícula {MAT} de la carrera de {CARR} a sido ACEPTADO")
        else:
            print(f"El alumno {NOM}  no a sido ACEPTADO")
            
elif CARR =="Administración":
        SEM > 5
        if PROM >= 8.5:
             print(f"El alumno {NOM} con la matrícula {MAT} de la carrera de {CARR} a sido ACEPTADO")
        else:
            print(f"El alumno {NOM}  no a sido ACEPTADO")
print("FIN DEL PROGRAMA")
