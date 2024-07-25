import os
"""
Ejercicio
"""
'''
# Crear Fichero
file_name = "nazelord.txt"

# Abrir fichero
with open(file_name, 'w') as file:
    file.write("Carlos Sanchez")
    file.write("\n21")
    file.write("\nPython")

# Leer fichero
with open(file_name, 'r') as file:
    print(file.read())

# Borrar fichero
os.remove(file_name)
'''

"""
Extra
"""

# Programa de gestion de ventas



# Crear base de datos
datos = "datos.txt"
open(datos, 'a')

def main():
    while True:
        print("\nGestion de Ventas")
        print("\n1. Productos")
        print("\n2. Calcular Ventas")
        print("\n3. Salir")
        option = int(input("Elija una opcion: "))
        match option:
            case 1:
                productos()
            case 2:
                calcular_ventas()
            case 3:
                print("Saliendo...")
                os.remove(datos)
                break

def productos():
    while True:
        print("\nGestion de Productos")
        print("\n1. Añadir Producto")
        print("\n2. Mostrar Productos")
        print("\n3. Actualizar Productos")
        print("\n4. Eliminar Producto")
        print("\n5. Volver")
        option = int(input("Elija una opcion: "))
        match option:
            case 1:
                name = input("Introduce el nombre del producto: ")
                quantity = int(input("Introduce la cantidad vendida: "))
                price = float(input("Introduce el precio del producto: "))
                with open(datos, 'a') as file:
                    file.write(f"{name}, {quantity}, {price}\n")
            case 2:
                with open(datos, 'r') as file:
                    name = input("Nombre: ")
                    for line in file.readlines():
                        if line.split(', ')[0] == name:
                            print(line)
                            break
            case 3:
                name = input("Introduce el nombre del producto: ")
                quantity = int(input("Introduce la cantidad vendida: "))
                price = float(input("Introduce el precio del producto: "))
                with open(datos, 'r') as file:
                    lines = file.readlines()
                with open(datos, 'w') as file:
                    for line in lines:
                        if line.split(', ')[0] == name:
                            file.write(f"{name}, {quantity}, {price}\n")
                        else:
                            file.write(line)
            case 4:
                name = input("Introduce el nombre del producto: ")
                with open(datos, 'r') as file:
                    lines = file.readlines()
                with open(datos, 'w') as file:
                    for line in lines:
                        if line.split(', ')[0]!= name:
                            file.write(line)
                print("Producto eliminado correctamente")
            case 5:
                print("Volviendo a Menu Principal")
                break


def calcular_ventas():
    while True:
        print("\nCalcular Ventas")
        print("\n1. Calcular Ventas Totales")
        print("\n2. Calcular Ventas por Producto")
        print("\n3. Volver a Menu Principal")
        option = int(input("Elija una opcion: "))
        match option:
            case 1:
                total = 0
                with open(datos, "r") as file:
                    for lines in file.readlines():
                        components = lines.split(", ")
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                print(f"El total es: {total}")
            case 2:
                name = input("Nombre: ")
                total = 0
                with open(datos, "r") as file:
                    for lines in file.readlines():
                        components = lines.split(", ")
                        if components[0] == name:
                            quantity = int(components[1])
                            price = float(components[2])
                            total += quantity * price
                            break
                print(f"El total es: {total}")
            case 3:
                print("Volviendo a Menu Principal")
                break

# Abrir base de datos

main()