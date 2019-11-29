CONT=0
S1= float(input(" Ingresa el sueldo del empleado:$"))
S2= float(input(" Ingresa el sueldo del empleado:$"))
S3= float(input(" Ingresa el sueldo del empleado:$"))
S4= float(input(" Ingresa el sueldo del empleado:$"))
S5= float(input(" Ingresa el sueldo del empleado:$"))
AC=S1+S1+S2+S3+S4+S5
PROM = AC/5
if S1>PROM:
    CONT=+1
if S2>PROM:
    CONT=+1
if S3>PROM:
    CONT=+1
if S4>PROM:
    CONT=+1
if S5>PROM:
    CONT=+1
print("Los sueldos superiores al promedio son:", CONT)
print("FIN DEL PROGRAMA")

