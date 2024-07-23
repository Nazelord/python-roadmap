""" 
Funciones Definidas por el usuario
"""

# Definir Funciones simples

def greet():
    print("Hola, Python")

greet()

# Funcion con Retorno

def return_greet():
    return "Hola, Python"

print(return_greet())

# Funcion con argumento

def arg_greet(name):
    print(f"Hola, {name}")

a = "Carlos"

arg_greet(a)

# Funcion con argumentos

def args_greet(greet, name):
    print(f"{greet}, {name}")

args_greet("Hi","Brais")
args_greet(name="Brais", greet="Hi")

# Funcion con predeterminado

def default_arg_greet(name="Pyton"):
    print(f"Hola, {name}")

default_arg_greet()

# Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi","Brais"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()

print(greet)
print(name)

# con numero variable de argumentos

def variable_arg_greet(*name):
    for name in name:
        print(f"Hello, {name}")

variable_arg_greet("Python", "Marcos", "Andres")

# con un numero variable de argumentos con palabra clave

def variable_key_arg_greet(**name):
    for key, value in name.items():
        print(f"{value} ({key})!")

variable_key_arg_greet(
    Language="python",
    name="Brais",
    alias="MoureDev", 
    age=36
)

# Funciones dentro de funciones

def outer_function():
    def inner_function():
        print("Función interna: Hola, Python!")
    inner_function()

outer_function()

# Funciones del lenguaje (built-in)

print(len("MoureDev")) #Función len
print(type(36)) #Función type
print("MoureDev".upper()) #Función upper

# Variables locales y globales

global_var = "Python"

print(global_var)

def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")

hello_python()

# Reto extra

def print_numbers(text1, text2):
    count = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(text1 + " " + text2)
        elif i % 3 == 0:
            print(text1)
        elif i % 5 == 0:
            print(text2)
        else:
            print(i)
            count += 1
    return count

print(print_numbers("fizz", "Buzz"))