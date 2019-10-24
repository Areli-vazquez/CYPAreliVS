SUMOTR= 0
SUMPOS = 0
CUEPOS = 0
N= int(input("Ingresa el número de datos de la lista:"))
I = 1
for I in range(1, N, 1):
    NUM = int(input("El número es:"))
    if NUM > 0:
        SUMPOS += NUM
        CUEPOS += 1
        I +=1 
    else:
        SUMOTR += NUM
        I += 1
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = (SUMPOS/CUEPOS)
print("Total de números positivos:", CUEPOS)
print("El promedio de los números positivos es:" ,PROPOS)
print("El promedio general de todos los numeros es:" , PROGEN)
print("FIN DEL PROGRAMA")

