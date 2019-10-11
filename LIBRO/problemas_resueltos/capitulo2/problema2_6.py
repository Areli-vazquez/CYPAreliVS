A = int(input("Dame un número positivo:"))
if A == 0:
    print(f"El número {A} es NULO.")
else:
    if -1 ** A > 0:
        print(f"El número {A} es PAR.")
    else:
        print(f"El número {A} es IMPAR.")
print("FIN DEL PROGRAMA")
