NUM = int(input("Ingresa un número:"))
if NUM > 0: 
    while(NUM != 1):
        print("El numero es:", NUM)
        if (-1 ** NUM) >0: 
            NUM = NUM /2
        else:
            NUM = (NUM *3) + 1
    NUM = bool(int(input("Hay otro número(1= Sí, no=0):")))
else:
    print(f"{NUM}, TIENE QUE SER UN ENTERO POSITIVO")
print("FIN DEL PROGRAMA")


