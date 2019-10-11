A = int(input("Dame el primer nùmero entero:"))
B = int(input("Dame el segundo nùmero entero:"))
C = int(input("Dame el tercer nùmero entero:"))
if A > B:
    if A > C:
        print(f"El nùmero {A} es el mayor")
    else:
        if A == C:
            print(f"Los nùmeros {A} y {C} son los mayores.")
        else:
            print(f"El nùmero {C} es el mayor")
else: 
    if A == B:
        if A > C:
            print(f"Los numeros {A} y {B} son los mayores.")
        else:
            if A == C: 
                print(f"Los numeros {A},{B} y {C} son iguales.")
            else: 
                print(f"El nùmero {C} es el mayor.")
    else:
        if B > C:
            print(f"El nùmero {B} es el mayor.")
        else: 
            if B == C:
                print(f"Los nùmeros {B} y {C} son los mayores.")
            else:
                print(f"El nùmero {C} es el mayor")
print("FIN DEL PROGRAMA")

