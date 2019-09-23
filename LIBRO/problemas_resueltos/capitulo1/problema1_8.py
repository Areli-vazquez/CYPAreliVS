X1 = float(input("Ingresa la coordenada 'X' del punto 1:"))
Y1 = float(input("Ingresa la coordenada 'Y' del punto 1:"))
X2 = float(input("Ingresa la coordenada 'X' del punto 2:"))
Y2 = float(input("Ingresa la coordenada 'Y' del punto 2:"))
DIS = ((X1 - X2) **2 + (Y1 - Y2) **2) ** 0.5
print(f"La distancia entre el punto 1 ({X1},{Y1}) y el punto 2 ({X2},{Y2}) es de : {DIS} cm.")
