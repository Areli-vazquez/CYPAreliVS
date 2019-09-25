edad = int(input("Dame tu edad:"))
INE = bool(int(input("TIenes INE (0  no / 1  si):")))

if edad >= 18 and INE == True:
    print("Es mayor de edad")
    print("Puedes entrar al antro")
    print("Fin del programa")
