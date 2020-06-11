

# CONDICIONAL IF

# Ejemplo 1

print("#####EJEMPLO1#####")

color = input("Adivina cual es mi color favorito: ")

if color == "rojo":
    print("ENHORABUENA, el color es rojo")
else:
    print("INCORRECTO, intentelo de nuevo")

# Ejemplo 2

print("#####EJEMPLO2#####")

year = int(input("¿En que año estamos?"))

if year < 2021:
    print("Estamos antes del 2021")
else:
    print("Es un año posterior al 2021")

# Ejemplo 3

print("#####EJEMPLO3#####")

nombre = "Alvaro Rueda"
ciudad = "Sevilla"
continente = "Europa"
edad = 20
mayoriaEdad = 18

if edad >= mayoriaEdad:
    print(nombre+" es mayor de edad")

    if continente != "Europa":
        print("El usuario no es Europeo")
    else:
        print("El usuario es Europeo y vive en "+ciudad)
else:
    print("No es mayor de edad")

# Ejemplo 4

print("#####EJEMPLO4#####")

dia = int(input("¿Que dia es?"))

if dia ==1:
    print("El dia es lunes")
elif dia ==2:
    print("El dia es martes")
elif dia ==3:
    print("El dia es miercoles")
elif dia ==4:
    print("El dia es jueves")
elif dia ==5:
    print("El dia es viernes")
else:
    print("Es fin de semana")

#Ejemplo 5

print("#####EJEMPLO5#####")

edadMinima = 18
edadMaxima = 65
edadOficial = 17

if edadOficial >= 18 and edadOficial < 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")