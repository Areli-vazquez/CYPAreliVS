PRI = 0
SEG = 1
I = 3
for I in range(3, 180, 1):
    SIG =PRI + SEG
    PRI = SEG
    SEG = SIG
    I += 1
    print("El siguiente número de la serie es:" , SIG)
print("FIN DEL PROGRAMA")
