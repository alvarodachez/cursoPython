#
# for variable in elemento_iterable (lista,rango,etc)
#    BLOQUE DE INSTRUCCIONES
#

cont = 0
res = 0
for cont in range(0, 5):
    print("Voy por el "+str(cont))
    res = res + cont

print(f"El resultado es: {res} ")

# EJEMPLO TABLAS DE MULTIPLICAR

print("EJEMPLO DE TABLAS DE MULTIPLICAR")

numero = input("Vamos a mostrar la tabla de multiplicar de: \n")
itarador = 0
for iterador in range(0,10):
    print(str(numero) + "x" + str(iterador) +" = "+ str(iterador * int(numero)))
    