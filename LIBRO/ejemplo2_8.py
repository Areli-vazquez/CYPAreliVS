CATE = int(input("Categoria del trabajador(1-4):"))
SUE = float(input("Sueldo del trabajador:"))
NSUE = 0

if CATE == 1:
    NSUE = SUE * 1.15
elif CATE == 2:
    NSUE = SUE * 1.10
elif CATE == 3:
    NSUE = SUE * 1.08
elif CATE == 4:
    NSUE = SUE * 1.07
print(f"El nuevo sueldo es de: ${NSUE} por tener la categoria: {CATE}")
print("FIN DEL PROGRAMA")



