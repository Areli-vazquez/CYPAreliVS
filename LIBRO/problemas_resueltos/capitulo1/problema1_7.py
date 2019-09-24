L1 = float(input("Ingresa la medida del lado 1 del triángulo:"))
L2 = float(input("Ingresa la medida del lado 2 del triángulo:"))
L3 = float(input("Ingresa la medida del lado 3 del triángulo:"))
S = (L1 + L2 + L3)/2
AREA = (S * (S - L1) * (S - L2) * (S - L3)) ** 0.5
print(f"El área del triángulo con la medida de los lados 1: {L1} cm, 2: {L2} cm, 3: {L3} cm, es de {AREA} cm.")
