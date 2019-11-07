#Argumentos
def sumar( x , y ):
    z = x + y
    return z

def restar ( x , y ):
    return x - y

def mi_print( texto) :
    print(f"Este es mi print:{texto}")

#None
def multiplica (valor , veces):
    if veces == None :
        print("Debes enviar el 2do argumento de la función")
    else:
        print(valor * veces)

def comanda(mesa, comensal, entrada, medio, fuerte, postre):#argumentos variables internas dentro del parentesis
    print(f"Mesa:{mesa}, comensal: {comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")
def comandas(mesa, comensal, entrada, medio, fuerte, postre="Gela de limòn"):
    print(f"Mesa:{mesa}, comensal: {comensal}")
    print(f"\t Entrada:{entrada}")
    print(f"\t Segundo tiempo: {medio}")
    print(f"\t Plato fuerte:{fuerte}")
    print(f"\t Postre:{postre}")
"""
def comanda2(**comida):#diccionario
    print(comida)
    """
def comanda2(**comida):#diccionario
    llaves = comida.keys()
    for elem in llaves:
        print(elem, "-->",comida[elem])#se combino elem y llaves
        

"""
def imprime_argumentos(*argumentos):
    print('----->' ,argumentos, '<-----')
    
def imprime_argumentos(*argumentos):#for con interacción
    for ele in argumentos:
        print(ele)
"""
def imprime_argumentos(*argumentos): #index largo de listas con len
    for index in range (len(argumentos)):
        print(argumentos[index])




#Parametros
a = 10
b = 5
c = sumar(a,b)
print(f"La suma de {a} y {b} es: {c}")
c = restar(a,b)
print(f"La resta de {a} y {b} es: {c}")
mi_print("Hola")
#None
multiplica(10, 3)
multiplica(10, None)
multiplica('Hola', 3)
#comanda
comanda(2,1, "Ensalada", "sopa de rana","filete de pompa de oso","pastel de chocholate")#Parametros valores adquiridos dentro del parentesis
comanda("Ensalada", "sopa de rana","filete de pompa de oso","pastel de chocholate",2,1)
comanda(entrada="Ensalada", medio="sopa de rana",fuerte= "filete de pompa de oso",postre="pastel de chocholate", mesa=2, comensal=1)#Parametros valores adquiridos dentro del parentesis
comandas(3,1, "Ensalada", "sopa de rana","filete de pompa de oso")
comanda2(entrada="Ensalada", medio="sopa de rana",fuerte= "filete de pompa de oso",postre="pastel de chocholate", mesa=2, comensal=1, bebida='coca ligth')#diccionario

#tuplas
imprime_argumentos('Hola', True, 3.1416,1000, {'id': 'sc01', 'nombre':'Juan'})
imprime_argumentos()



