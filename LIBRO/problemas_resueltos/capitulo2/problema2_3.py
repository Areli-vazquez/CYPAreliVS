A = float(input("Dame el valor del coeficiente 'a'(diferente de 0):"))
B = float(input("Dame el valor del coeficiente 'b'(diferente de 0):"))
C = float(input("Dame el valor del coeficiente 'c'(diferente de 0):"))
DIS = B**2-4*A*C
X1 = ((-B)+DIS**0.5)/2*A
X2 = ((-B)-DIS**0.5)/2*A
if DIS >= 0:
    print(f"La primera raíz real de la ecuación es X1: {X1}")
    print(f"La segunda raíz real de la ecuación es X2: {X2}")
print("Fin del programa")

