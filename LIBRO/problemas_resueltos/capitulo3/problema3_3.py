SERIE = 0
N = int(input("Dame el número entero:"))
BAND = 'T'
I = 1
for I in range(1, N, 1):
    if BAND == 'T':
        I +=1
        SERIE += 1/I
        BAND =='F'
        
    else: 
        SERIE -= 1/I
        BAND == 'T'
        I +=1
print("EL resultado de la serie es:" ,SERIE)
print("FIN DEL PROGRAMA")

