SUMPAR = 0
SUMIMP = 0
CUEPAR = 0 
PROPAR = 0
I = 1
for I in range(1, 270, 1):
    NUM = int(input("Dame un número entero:"))
    if NUM % 2 == 0:
        SUMPAR += NUM
        CUEPAR += 1
        I += 1
        PROPAR = SUMPAR/CUEPAR
    else:
          SUMIMP += NUM
          I += 1

print("El promedio es de:", PROPAR)
print("La suma impar es:", SUMIMP)
print( "FIN DEL PROGRAMA")
