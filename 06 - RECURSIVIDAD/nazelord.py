"""
Ejercicio
"""

def countdown(number: int):
    if number >= 0:
        print(number)
        countdown(number - 1)     
    
#countdown(100)   

'''
Reto extra
'''

# Factorial

def factorial(number: int) -> int:
    if number < 0:
        return("Los numeros negativos no son validos")
    elif number == 0:
        return(1)
    else:
        return number * factorial((number - 1))    

print(factorial(1))


# Fibonacci

def fibo(number: int) -> int:
    if number <= 0:
        print(("La posicion no debe ser Negativo"))
        return 0
    elif number == 1:
        return(1)
    elif number == 2:
        return(1) 
    else:
        return fibo((number - 1)) + fibo((number - 2)) 

print(fibo(10))