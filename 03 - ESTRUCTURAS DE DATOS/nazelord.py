# Listas | Flexible

my_list = ['Brais','Black','Wolfy','Visionos']
print(my_list)

my_list.append("Castor") # Insercion
print(my_list)

my_list.remove("Brais") # Eliminacion
print(my_list)

print(my_list[1]) # Acceso

my_list[1] = "Cuervillo" # Actualizacion
print(my_list)

my_list.sort() # Ordenamiento
print(my_list)

# Tuplas | No es variable

my_tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1]) # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple)) # Ordenamiento
print(my_tuple) 
print(type(my_tuple))

# Sets / Hash Sets | No ordenada, no existen duplicados
my_set = {"Brais", "Moure","@Mouredev","36"}
print(my_set)
my_set.add("mouredev@gmail.com") # Insercion
my_set.add("mouredev@gmail.com")
print(my_set)
my_set.remove("Moure") # Eliminacion
print(my_set)
print(type(my_set))

# Diccionarios | Clave-Valor

my_dict = {
    "Name":"Brais", 
    "Surname":"Moure",
    "Alias":"@Mouredev",
    "Age":"36"
}

my_dict["email"] = "mouredev@gmail.com" # Insercion
print(my_dict)
del my_dict["Surname"] # Eliminacion
print(my_dict)
print(my_dict["Name"])
my_dict["age"] = "37" # Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(type(my_dict))

# Reto Extra

def my_agenda():
    agenda = {}

    def insert_number():
        while True:
            phone = input("Introduce el numero del contacto:")
            if phone.isdigit and len(phone) > 0 and len(phone) <= 11:
                agenda[name] = phone
                break
            else:
                print("Debes introducir un numero de telefono con un maximo de 11 digitos")

    while True:
        print("\nAgenda")
        print("1. Buscar contacto")
        print("2. Insertar contacto")
        print("3. Actualizar contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
    
        option = input("\nElija una opcion: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El numero de telefono de {name} es: {agenda[name]}")
                else:
                    print(f"El nombre del contacto {name} no existe")
                
            case "2":
                name = input("Introduce el nombre del contacto:")
                insert_number()
                
            case "3":
                name = input("Introduce el nombre del contacto a actualizar: ")
                if name in agenda:
                    insert_number()
                else:
                    print(f"El nombre del contacto {name} no existe")
                
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El nombre del contacto {name} no existe")
                
            case "5":
                print("Saliendo de la agenda...")
                break
            case _:
                print("Opcion No Valida. Elige una opcion del 1 al 5")
            
    

my_agenda()    