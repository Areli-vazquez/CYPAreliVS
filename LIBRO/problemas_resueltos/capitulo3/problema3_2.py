BAND = 'T'
SUMSER = 0
I = 2
while (I <= 1800):
    SUMSER += 1
    print("incremento de valor:" , I)
    if BAND == 'T' :
        BAND = 'F' 
        I += 3
    else:
        BAND = 'T' 
        I += 2
print("Los términos de la serie son:" , SUMSER)
print("FIN DEL PROGRAMA")
