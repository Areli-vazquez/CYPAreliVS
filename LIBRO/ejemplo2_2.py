SUE = float(input("Ingresa el sueldo del trabajador:$"))
AUM = SUE * 0.15
NSUE = SUE + AUM
if SUE < 1000:
    print(f"Tu nuevo sueldo es de: ${NSUE}")
print("FIN DEL PROGRAMA")
