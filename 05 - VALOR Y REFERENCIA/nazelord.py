# Tipos de dato por valor , El original no cambia

my_int_a = 10
my_int_b = my_int_a
# my_int_b = 20
#my_int_a = 30
print(my_int_a)
print(my_int_b)

'''
number = 1
string = "String"
float1 = 1.0
booleano = True
'''

# Tipos de datos por referencia

my_list_a = [10,20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

''' 
list1 = [1, 2, 3]
tuple1 = (1,2,3)
dict1 = {
    "name": "John",
    "age": 30
}
set1 = {Hola,mundo,python}
'''

# Funcion con datos por valor

my_int_c = 10

def my_int_func(my_int: int):
    my_int = 20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

# Funcion por referencia

def my_list_func(my_list: list):
    my_list.append(30)
    my_list_d = my_list
    my_list_d.append(40)
    print(my_list)
    print(my_list_d)

my_list_c = [10,20]
my_list_func(my_list_c)
print(my_list_c)


# Extra

# Por Valor

def value(value_a: int, value_b: int) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_int_d = 10
my_int_e = 20
my_int_f, my_int_g = value(my_int_d,my_int_e)
print(f"{my_int_d}, {my_int_e}")
print(f"{my_int_f}, {my_int_g}")

# Por Referencia

def ref(value_a: list, value_b: list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


my_list_e = [10, 20]
my_list_f = [30, 40]
my_list_g, my_list_h = value(my_list_e,my_list_f)
print(f"{my_list_e}, {my_list_f}")
print(f"{my_list_g}, {my_list_h}")