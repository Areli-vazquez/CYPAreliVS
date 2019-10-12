SUE = float(input("Ingresa el sueldo básico del trabajador:$"))
CATE = int(input("Ingresa la categoria del trabajador:"))
HE = int(input("Ingresa las horas extra:"))
if CATE == 1:
    PHE = 30
    HE < 30
    NSUE = SUE + HE *PHE
    print(f"El trabajador con la categoría {CATE} tendrá un sueldo total de : ${NSUE}, por tener {HE} horas extra")
elif CATE == 2:
    PHE = 38
    HE > 30
    NSUE = SUE + 30 *PHE
    print(f"El trabajador con la categoría {CATE} tendrá un sueldo total de : ${NSUE}, por tener {HE} horas extra")
elif CATE == 3:
    PHE = 50
    HE > 30
    NSUE = SUE + 30 *PHE
    print(f"El trabajador con la categoría {CATE} tendrá un sueldo total de : ${NSUE}, por tener {HE} horas extra")
elif CATE == 4:
    PHE = 70
    HE > 30
    NSUE = SUE + 30 *PHE
    print(f"El trabajador con la categoría {CATE} tendrá un sueldo total de : ${NSUE}, por tener {HE} horas extra")
elif CATE >=5:
    PHE = 0
    HE < 30
    NSUE = SUE + HE *PHE
    print(f"El trabajador con la categoría {CATE} tendrá un sueldo total de : ${NSUE}, por tener {HE} horas extra")
print("FIN DEL PROGRAMA")
