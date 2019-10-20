SUMPAR = 0
SUMIMP = 0
CUEPAR = 0 
PROPAR = 0
I = 1
for I in range(1, 10, 1):
    NUM = int(input("Ingresa un número entero"))
    while I <= 10:
        if (-1 ** NUM) > 0:
            SUMPAR += NUM
            CUEPAR += 1
            print("El promedio total es: PROPAR")
        else: 
            if ( -1 ** NUM ) <0:
                SUMIMP += NUM
                print("La suma impar es:", SUMIMP)
print( "FIN DEL PROGRAMA")

    
            


           
