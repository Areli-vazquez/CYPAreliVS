COMPRA = float(input("Ingresa el monto de la compra: $"))

if COMPRA < 500:
    print(f"El cliente debe pagar: ${COMPRA}, no tiene ningún descuento.")
else:
    if COMPRA <=1000:
        PAGAR = COMPRA - (COMPRA * 0.05)
        print(f"El cliente debe pagar: ${PAGAR}, teniendo el descuento de 5%.")
    else: 
        if COMPRA <=7000:
            PAGAR = COMPRA - (COMPRA * 0.11)
            print(f"El cliente debe pagar: ${PAGAR}, teniendo el descuento de 11%.")
        else:
            if COMPRA <=15000:
                PAGAR = COMPRA - (COMPRA * 0.18)
                print(f"El cliente debe pagar: $ {PAGAR}, teniendo el descuento de 18%.")
            else:
                PAGAR = COMPRA - (COMPRA * 0.25)
                print(f"El cliente debe pagar: ${PAGAR}, teniendo el descuento de 25%.")
print("FIN DEL PROGRAMA")


