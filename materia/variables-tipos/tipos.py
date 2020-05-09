nada = None
cadena = "Hola soy alvaro"
entero = 20
flotante = 4.5
booleano = True
lista = [10,20,30,40,50]
mixList = [44,"hola",50,"adios"]
tupla = ("no","cambian","las","tuplas")
diccionario = {
    "nombre":"Alvaro",
    "apellidos":"Rueda",
    "edad":"20"
}
rango = range(9)
dato_byte = b"Probando"

#IMPRIMIR VARIABLE
print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(mixList)
print(tupla)
print(diccionario)
print(rango)
print(dato_byte)
#IMPRIMIR TIPO DE DATO
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(mixList))
print(type(tupla))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

#CONVERTIR TIPOS DE DATOS
texto = "hola"
num = 10
#lo convierto a string para poder imprimirlo (solo concatena variables del mismo tipo)
num = str(num)
print(texto +" "+num)
#lo vuelvo a pasar a entero
num = int(num)
print(type(num))