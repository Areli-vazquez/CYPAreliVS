# arreglos
# Lectura
# escritura/ Asignaciòn
# actualizaciòn : insercciòn, eliminación , modificación
# ordenamiento
# búsqueda

# escritura
frutas =["zapote", "manzana", "pera", "aguacate", "durazno", "uva", "sandia"]

#lectura selector [indice]
print(frutas[2])
# Lectura con for
# for opciòn 1

for indice in range(0, 7,1):
    print(frutas[indice])
print("--------")

#for opciòn 2 -- por un iterador for each

for fr in frutas:
    print(fr)

# asignación
frutas[2] ="Melòn"
print(frutas)

# insercción al final
frutas.append("naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"limón")
print(frutas)
print(len(frutas))
frutas.insert(0, "mamey")
print(frutas)
print(len(frutas))
#eliminación con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas[2]="limón"
frutas.append("limón")
frutas.append("limón")
print(frutas)
frutas.remove("limón")
print(frutas)

# ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

# busqueda
print(f"uva está en la posiciòn. {frutas.index('uva')}")
print(f"El limòn esta { frutas.count('limón') } veces en la lista")


# concatenar
print(frutas)
otras_frutas = ("Rambutan","mispero","Lichi","Pitaya")
frutas.extend(otras_frutas)
print(frutas)

#copiar

copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)


otra_copia=frutas.copy()
otra_copia.append("fresa")
print(frutas)
print(otra_copia)

