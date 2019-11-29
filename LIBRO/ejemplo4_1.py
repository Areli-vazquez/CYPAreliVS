AC = 0
I =1
S=0
for I in range (1,5,1):
    AC=+S
    I=+1
PROM = AC /5
CONT = 0
I = 1
for I in range(1,5,1):
    S= float(input( "ingresa el sueldo del empleado:"))
    if S > PROM :
        CONT =+1
    else:
        I=+1
print("los sueldos superiores son:", CONT)
print("FIN DEL PROGRAMA")
