NOM = 0
SUE = float(input("Ingresa tu sueldo:$"))
while(SUE % -1):
    if SUE < 1000:
        NSUE = SUE * 1.15
        NOM += NSUE
    else:
        NSUE= SUE * 1.12
        NOM += NSUE
    SUE = bool(int(input("Hay otro sueldo?(si=1, no=0)")))
print("Tu nuevo sueldo es:" , NSUE)
print("El sueldo de todos los trabajadores es:" , NOM)
print("FIN DEL PROGRAMA")

