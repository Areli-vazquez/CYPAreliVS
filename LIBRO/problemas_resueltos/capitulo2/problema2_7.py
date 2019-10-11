A = int(input("Dame el primer número:"))
B = int(input("Dame el segundo número:"))
C = int(input("Dame el tercer número:"))
if A < B:
    if B < C:
        print(f"Los números están en orden creciente.")
    else:
        print(f"Los números no están en orden creciente.")
else:
    print(f"Los números no están en orden creciente.")
print("FIN EL PROGRAMA")



