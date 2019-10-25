NOM =0
SUE = float(input("Ingresa tu sueldo:$"))
while(SUE !=-1):
    if SUE <=1000:
        NSUE = SUE*1.15
    else:
        if SUE >=1000:
            NSUE =SUE*1.12
    NOM +=NSUE
    print("Tu nuevo sueldo es:", NSUE)
    SUE = float(input("Hay otro sueldo:$"))
print("El nuevo sueldo de los trabajadores es:" , NOM)
print("FIN DEL PROGRAMA")

