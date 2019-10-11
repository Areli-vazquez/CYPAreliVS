PREBAS = float(input("Ingrese el precio del producto: $"))
if PREBAS >500:
    IMP = 20 * 0.30 + (PREBAS - 40) * 0.50
    PRETOT = PREBAS + IMP
    print(f"El cliente debe pagar: ${PRETOT}, teniendo el 50% de impuesto: {IMP}.")
else: 
    if PREBAS > 40:
        IMP = 20 * 0.30 + (PREBAS - 40) * 0.40
        PRETOT = PREBAS + IMP
        print(f"El cliente debe pagar: ${PRETOT}, teniendo el 40% de impuesto: {IMP}.")
    else:
        if PREBAS > 20:
            IMP = (PREBAS - 20) * 0.30
            PRETOT = PREBAS + IMP
            print(f"El cliente debe pagar: ${PRETOT}, teniendo el 30% de impuesto: {IMP}.")
        else:
            IMP = 0
            print(f"El cliente debe pagar:$ {PREBAS} , no tiene ningún impuesto: {IMP}.")
print("FIN DEL PROGRAMA")
