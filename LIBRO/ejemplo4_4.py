N=[1,2,3,4,6,7,8]


if N >=1:
    X = int(input("elemento que se modifica:"))
    I=1
    BAND= False
    while (1<=N) and (BAND == False):
        if A[I]== X:
            Y = int(input("Elemento que reemplza:"))
            A[I]= Y
            BAND= True
        else:
            I=+1
    if BAND == False:
        print(f"el elemento: {X}, no está en el arreglo")
    else:
        print(f"El arreglo: {A} , esta vacío")
print("FIN DEL PROGRAMA")
