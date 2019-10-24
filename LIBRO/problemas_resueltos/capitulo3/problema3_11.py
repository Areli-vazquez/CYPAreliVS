CAN1 =0
CAN2 =0
CAN3 =0
CAN4= 0

VOTO =int(input("Escriba para que candidato será su voto(1-4):"))
while(VOTO !=0):
    if VOTO == CAN1:
        CAN1 +=1
    elif VOTO == CAN2:
        CAN2 +=1
    elif VOTO == CAN3:
        CAN3 +=1
    elif VOTO == CAN4:
        CAN4 +=1
    VOTO = bool(int(input("Hay otro voto? ")))
SUMV = CAN1 + CAN2 + CAN3 + CAN4
POR1 = (CAN1/SUMV)*100
POR2 = (CAN2/SUMV)*100
POR3 = (CAN3/SUMV)*100
POR4 = (CAN4/SUMV)*100
print("VOTOS CANDIDATO 1:", CAN1, "PORCENTAJE:",POR1)
print("VOTOS CANDIDATO 2:", CAN2, "PORCENTAJE:",POR2)
print("VOTOS CANDIDATO 3:", CAN3, "PORCENTAJE:",POR3)
print("VOTOS CANDIDATO 4:", CAN4, "PORCENTAJE:",POR4)
print("CANTIDAD DE VOTANTES:", SUMV)
print("FIN DEL PROGRAMA")

