# En este archivo py veremos las variables
# Para empezar, las variables como yo las conozco son
# un espacio que la memoria reserva para almacenar valores
# o datos que nos permitirán realizar distintos
# tipos de operaciones o manipularlas.
# Dicho de otra forma, usamos las variables como cajas
# donde almacenamos lo que queremos, puede ser
# una cadena, un número, un valor booelano o una estructura
# mas grande (tupla, listas, diccionarios, etc)

# VARIABLES

print("Variables")

Saludo = "Hola, bienvenido a la escuela de Python"
# "Saludo" es una variable (espacio en memoria) que guarda el mensaje que está
# a la derecha del igual "="
print(type(Saludo))  # Imprime el tipo de dato que contiene la variable
print(Saludo)    # Imprime el contenido de la variable

opcioBool = False
print(opcioBool)  # Imprime False en consola

numEntero = 15
numDecimal = 15.12
print(type(numEntero))  # int
print(type(numDecimal)) # float
print(numEntero)   # 15
print(numDecimal)  # 15.12

# Concatenar e imprimir las variables en formato string
# Forma válida 1, la forma mas utilizada para imprimir datos aunque 
# no por eso la única
print(Saludo, opcioBool, numDecimal, numEntero)
# Forma válida 2, en este caso se hace una conversion a string
# de las variables boolenas y numéricas, en el anterior caso, la conversion
# ya viene implícita
print(Saludo + str(opcioBool) + str(numDecimal) + str(numEntero))

# Probaré algunas funciones del sistema de Python
print(len(Saludo))
print(pow(12, 3))
print(abs(-123))

# Podemos crear e inicializar variables en una sola línea
nombre, apellido, edad, hombre = "Angel", "Alvarado", 25, True
# la anterior forma no es recomendada, así que no la usaremos mucho

print("Me llamo", nombre, apellido, " tengo", edad, "años")

# Python al ser un lenguaje debilmente tipado, nos permite cambiar los tipos
# de las variables previamente definidas

nombre = 15
apellido = False
hombre = 56.2

print(nombre, apellido, hombre)

# Entrada de datos por consola
# input, este método nos permite ingresar datos por consola con el teclado
# sin embargo, dicen que no es muy utilizado y por lo tanto, muy poco recomendado
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")

print("Tu nombre es:", nombre, apellido, "y tienes", edad, "años")

