"""
Ejercicio
"""

# Capturar el error

try:
    print(10/1)

    my_list = [1,2,3,4]
    print(my_list[4])
except Exception as e:
    print(f"Se ha producido un error: {e}")

'''
Extra
'''
class StrTypeError(Exception):
        pass
def process_params(parameters: list):

    if len(parameters) < 3:
        raise IndexError("Invalid parameters")
    elif parameters[1] == 0:
        raise ZeroDivisionError("Division by zero")
    elif type(parameters[2]) == str:
        raise StrTypeError("El Tercer elemento no puede ser una cadena de texto")

    print(parameters[2])
    print(parameters[0]/parameters[1])
    print(parameters[2] + 5)

try:
    process_params([1,1,3,4])
except IndexError as e:
    print("El numero de elementos de la lista debe ser mayor de 2")
except ZeroDivisionError as e:
    print("El segundo elemento de la lista no puede ser 0")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se ha producido un error inesperado: {e}")
else:
    print("No se ha producido ningun error")
finally:
    print("El programa finaliza sin detenerse")




