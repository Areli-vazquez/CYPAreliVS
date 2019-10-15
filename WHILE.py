otra = True
suma = 0
while(otra == True):
    cal = float(input("Calificación:"))
    suma += cal 
    otra = bool(int(input("Hay más alumnos(0 No, 1 si):")))
print("suma", suma)
print("FIN DEL PROGRAMA")

