NUM1 = int(input("Dame el primer número:"))
NUM2 = int(input("Dame el segundo número:"))
NUM3 = int(input("Dame el tercer número:"))

if NUM1 > NUM2 and NUM1 > NUM3:
    print(f"{NUM1} es el número mayor")
if NUM2 > NUM1 and NUM2 > NUM3:
    print(f"{NUM2} es el número mayor")
if NUM3 > NUM1 and NUM3 > NUM2:
    print(f"{NUM3} es el número mayor")
    print("Fin del programa")
    print("otra solución:")
if NUM1 != NUM2 and NUM1 > NUM3:
    print(f"{NUM1}, es el mayor")
else: 
    if NUM2 > NUM1 and NUM2 > NUM3:
        print("{NUM2}, es el mayor")
    else: 
        print(NUM3, "es el mayor")
    print("La misma pero simplificada:")
if NUM1 != NUM2 and NUM1 != NUM3 and NUM2 != NUM3:
    if NUM1 > NUM2 and NUM1 > NUM3:
        print(NUM1, "es el mayor")
    elif NUM2 > NUM1 and NUM2 > NUM3:
        print(NUM2, "es el mayor")
    if NUM3 > NUM2 and NUM3 > NUM1:
        print(NUM3, "es el mayor")
