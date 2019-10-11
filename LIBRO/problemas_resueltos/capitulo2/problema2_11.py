CLAVE = int(input("Ingresa la zona geográfica a la que se llamó(CLAVE):"))
NUMIN = int(input("Ingresa la duración de la llamada(minutos):"))
if CLAVE ==12:
    COST = NUMIN * 2
    print(f"El costo total de la llamada de {NUMIN} minutos es de: ${COST}")
elif CLAVE == 15:
        COST = NUMIN * 2.2
        print(f"El costo total de la llamada de {NUMIN} minutos es de: ${COST}")
elif CLAVE == 18:
        COST = NUMIN * 4.5
        print(f"El costo total de la llamada de {NUMIN} minutos es de: ${COST}")
elif CLAVE == 19:
        COST = NUMIN * 3.5
        print(f"El costo total de la llamada de {NUMIN} minutos es de: ${COST}")
elif CLAVE == 23:
        COST = NUMIN * 6
        print(f"El costo total de la llamada de {NUMIN} minutos es de: ${COST}")
elif CLAVE == 25:
        COST = NUMIN * 6
        print(f"El costo total de la llamada de {NUMIN} minutos es de: ${COST}")
elif CLAVE == 29:
        COST = NUMIN * 5
        print(f"El costo total de la llamada de {NUMIN} minutos es de: ${COST}")
print("FIN DEL PROGRAMA")
