"""
Operaciones
"""
s1 = "Hola"
s2 = "Python"

# Concatenación
print(s1 + " " + s2 + "!")

# Repetición

print(s1 * 3)

# Indexacion

print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (Porcion)

print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda

print("a" in s1)
print("i" in s1)

# Reemplazo

print(s1.replace("o","a"))

# Division
print(s2.split("t"))

# Mayusculas y minusculas
print(s1.upper())
print(s1.lower())
print("brais moure".title())
print("brais moure".capitalize())

# Eliminar espacios al principio y al final

print(" brais moure ".strip() + "@mouredev")

# Busqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Brais Moure @mouredev"

# Busqueda de posicion
print("Brais Moure @mouredev".find("moure"))
print("Brais Moure @mouredev".find("Moure"))
print("Brais Moure @mouredev".find("M"))
print("Brais Moure @mouredev".lower().find("m"))

# Busqueda de Ocurrencias
print(s3.lower().count("m"))

# Formatear cadena
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolar
print(f"Saludo: {s1}, lenguaje: {s2}!")

# Transformacion en lista de caracteres
print(list(s3))

# Transformacion de lista en cadena
l1 = [s1, " ", s2, "!"]
print("".join(l1))

# Transformaciones numericas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones Varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())

# Extra 

def check(word1: str, word2: str):
    #Palindromas
    print(f"{word1} es un palindromo: {word1 == word1[::-1]}")
    print(f"{word2} es un palindromo: {word2 == word2[::-1]}")

    # Anagramas
    print(f"{word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isograma
    print(f"{word1} es un isograma?: {len(word1) == len(set(word1))}")
    print(f"{word2} es un isograma?: {len(word2) == len(set(word2))}")

    word_dict = dict()
    for word in word1:
        word_dict[word] = word_dict.get(word,0)+1
    
    isogram = True
    values = list(word_dict.values())
    isogram_len = values[0]
    for word_count in values:
        if word_count != isogram_len:
            isogram = False
            break

check("radar","python")
check("amor","roma")