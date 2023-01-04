# OPERADORES

# Operadores aritméticos
print("4 + 3 =", 4 + 5)  # Obviamente es una suma
print("4 * 3 =", 4 * 3)  # Multiplicación
print("4 / 3 =", 4 / 3)  # División decimal o con residuo
print("4 - 3 =", 4 - 3)  # Resta
print("4 % 3 =", 4 % 3)  # Módulo o resto de una división
print("4 ** 3 =", 4 ** 3)  # Potenciación
print("4 // 3 =", 4 // 3)  # División entera

# También pueden ser usados para efectuar operaciones con cadenas
print("Hola muchachos " + str(5)) # concatena unicamente cadenas (string)
print("Hola " * 5)  # Multilica el mensaje 5 veces

# Operadores relacionales o comparativos
# Estos operadores me permiten comparar datos para averiguar sus equivalencias
print("45 mayor que 56 es " + str(45 > 56))
print("45 menor que 56 es", 45 < 56)
print("45 mayor o igual que 56 es " + str(45 >= 56))
print("45 menor o igual que 56 es", 45 <= 56)
print("45 igual que 56 es", 45 == 56)
print("45 distinto que 56 es", 45 != 56)

# Operadores lógicos o booleanos
# Existen varias operadores lógicos, provenientes del álgebra de Boole
# pero en este caso haremos uso principalmente de tres, and, or y not
print(10 < 11 and False)   # false
print("a" == "A" or True)  # true
print(45 != 12 and (False or (45 < 54)))  # true
print(34 > 10 and "true" == "false")  # false
print(not "Hola" > "hola" or 12.1 == 12.2)  # false

