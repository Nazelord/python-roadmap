# Creando Ejemplos de Operadores

# Operadores Aritméticos

print(f"Suma: 10 + 3 = {10+3}")

print(f"Resta: 32 - 11 = {32-11}")

print(f"Multiplicación: 3 * 7 = {3*7}")

print(f"División: 63 / 3 = {63/3}")

print(f"Division con redondeo: 63 // 3 = {63//3}")

print(f"Modulo: 10 % 3 = {10%3}")

print(f"Exponentes: 10 ** 3 = {10**3}")

# Operadores de Comparación
print(f"Igualdad: 10 == 3 es {10 == 3}" )

print(f"Desigualdad: 10 != 3 es {10 != 3}" )

print(f"Mayor Que: 10 > 3 es {10 > 3}" )

print(f"Menor Que: 10 < 3 es {10 < 3}" )

print(f"Mayor o Igual Que: 10 >= 10 es {10 <= 10}")

print(f"Menor o Igual Que: 10 <= 3 es {10 <= 3}" )

# Operadores Logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")

print(f"OR ||: 10 + 3 == 14 or 5 - 1 == 4 es {10+3 == 14 or 5 - 1 == 4}")

print(f"NOT !: not 10 + 3 == 14 es {not 10+3 == 14}")

# Operadores de Asignación

my_number = 11 # Asignacion
print(my_number)

my_number += 1 # Suma y Asignacion
print(my_number)

my_number -= 1 # Resta y Asignacion
print(my_number)

my_number *= 2 # Multiplicacion y Asignacion
print(my_number)

my_number /= 2 # Division y Asignacion
print(my_number)

my_number %= 2 # Modulo y Asignacion
print(my_number)

my_number **= 1 # Exponente y Asignacion
print(my_number)

my_number //= 1 # Division entera y Asignacion
print(my_number)

# Operadores de Identidad | Comparar el valor de la posicion de memoria

my_new_number = my_number

print(f"my_number is my_new_number es {my_number is my_new_number}")

print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de Pertenencia

print(f"'u' in 'mouredev'= {'u' in 'mouredev'}") 

print(f"'b' not in 'mouredev'= {'b' not in 'mouredev'}") 

# Operadores de Bit

a = 10 # 1010

b = 3 # 0011

print(f"AND: 10 & 3 = {10 & 3}") # 0010

print(f"OR: 10 | 3 = {10 | 3}") # 1011

print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001

print(f"NOT: ~10 = {~10}")

print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010

print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") #101000

"""
Estructuras de Control
"""

#Condicionales

my_string = "mouredev"

if my_string == "mouredev":
    print("my_string es 'MoureDev'")
elif my_string == "brais":
    print("my_string es 'Brais'")
else:
    print("my_string no es 'MoureDev'")

#Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones

try:
    print(10 / 0)
except:
    print("No se puede dividir entre 0")
finally:
    print("Ha finalizado el manejo de excepciones")    

# Extra

for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)

