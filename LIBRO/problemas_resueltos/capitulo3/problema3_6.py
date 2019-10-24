MAY = -100000 
MEN = 100000
N = int(input("¿Cuántos números enteros son?:"))
I = 1
for I in range(1, N, 1):
    NUM = int(input("Ingresa el número:"))
    if NUM > MAY :
        MAY = NUM
        if NUM < MEN:
            MEN = NUM 
            I += 1
print("El número mayor es:" , MAY)
print("El número menor es: " , MEN)
print("FIN DEL PROGRAMA")
