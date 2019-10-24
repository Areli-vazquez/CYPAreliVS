MED = 0
CHI = 0
GRA =0
N = int(input("Ingrese el número de ventas:"))
I = 1
for I in range(1, N, 1):
    V = float(input("Indique de cuánto fue su venta:$"))
    if V <= 200:
        CHI += 1
        
    else: 
        if V < 400:
            MED += 1
            
        else: 
            GRA += 1
    I += 1
print("El número de ventas chicas (-200) es de:" , CHI)
print("El número de ventas medianas (+200 pero -400) es de:", MED)
print("El número de ventas grandes (+400) es de:", GRA)
print("FIN DEL PROGRAMA")
