NUM =int(input("Ingresa un número:"))
if NUM > 0: 
    while (NUM !=1):
        if NUM % 2 == 0:
            NUM /=2
        else:
             NUM = (NUM *3) + 1
        print("El número es:", NUM)
else:
    print(NUM ,"TIENE QUE SER UN ENTERO POSITIVO")
print("FIN DEL PROGRAMA")


