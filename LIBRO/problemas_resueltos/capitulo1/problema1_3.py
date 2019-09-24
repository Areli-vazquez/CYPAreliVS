NOM = str(input("Indica el nombre del dinosaurio:"))
PES = float(input("Indica el peso del dinosaurio (en toneladas):"))
LON = float(input("Indica la longitud del dinosaurio (en pies):"))
PESKIL = PES*1000
LONMET = LON*0.3047
print(f"El peso en kilogramos del dinosaurio {NOM} es : {PESKIL} kilos, dado que el peso en toneladas es: {PES}")
print(f"La longitud en metros del dinosaurio {NOM} es : {LONMET} metros, dado que la longitud en pies es : {LON}")
        
