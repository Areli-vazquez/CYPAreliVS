#print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion format ()
4.- es con una variante de format()
"""
# con comas , concatenar agregando
# un espacio y haciendo casting de tipo 
edad = 20
nombre = "Areli"
estatura = 1.63
print(edad , estatura , nombre)
# con '+' hace lo mismo pero no
# realiza el cating automàtico
# no agrega espacio
print(str(edad) + str(estatura) +nombre)

#3.- funcion format()

print("nombre: {} edad: {} estatura: {} ".format(nombre, edad, estatura))

#4.- con una variante de format () simplificada

print (f"nombre: \"{nombre}\" \n edad:\t\t {edad}")

# print y el argumento end
print("solo hay 10 tipos de personas, las que saben binario y las que no", end="--  ")
print("otra linea")
