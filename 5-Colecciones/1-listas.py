# Estructura de datos I
# Listas - list()
# Documentación:
# https://docs.python.org/es/3.14/tutorial/datastructures.html
# https://www.w3schools.com/python/python_lists.asp

fruits = ['manzana', 'naranja', 'mango']
# índices     0          1         2

print("Fruta: ", fruits[1])
print("*" * 30)


for f in fruits:
    print("Fruta: ", f)
    # print("Fruta: ", f[:3])


data = ["Christian", 45, 1.7, True, ["Python", "JS", "C#"]] # -1 es list() anidada
# i =        0        1   2     3              4
# i =                                    0       1     2

print("*" * 30)
for d in data:
    print("Dato: ", d)
    
print("Estudiamos: ", data[4][0])
print("Tipo de dato: ", type(data[4][0]))

print("*" * 30)
matrix = [[1, 2, 3], [0, 0, 0], [4, 5, 6]] # ES UNA MATRIZ (matemáticas)
# Tipado dinámico, el siguiente sobre escribe el anterior
matrix = [[1, 2, 3], [0, 0, 0], [0, 0, 0]] # ES UNA MATRIZ (matemáticas)
other_matrix = [[1, 2], [0, 0, 0, 0], [4, 5, 6]] # NO ES UNA MATRIZ

print("*" * 30)
for line in matrix:
    print(f"Dato: ", line, "Índice: ", matrix.index(line))

print("*" * 30)
# lenght = longitud = len()
print(f"La matrix tiene {len(matrix)} filas.", f"Tipo: {type(len(matrix))}")
# La relación es longitud - 1 = último índice

for index in range(len(matrix)): # 0, 1, 2
    print(f"Dato: ", matrix[index], "Índice: ", index)

print("*" * 30)
# Agregar elemento
fruits.append("banana")
print(fruits)

fruits.insert(0, "kiwi")
print(fruits)

fruits.pop() # elimina el último
print(fruits)

fruits.pop(2) # elimina el pindice indicado
print(fruits)

#fruits.pop(15) # elimina el pindice indicado || IndexError: pop index out of range
#print(fruits)

# Propiedades:
# - Son ordenadas porque tienen índices.
# - Son heterogeneas porque aceptan distintos tipos de datos.
# - Son mutables porque puedo modificar sus elementos.
# - Admiten datos repetidos.

# Por comprensión
print("*" * 30)
# A = {x / x es un número par y 0 < x < 20} 2 4 6 8 10 12 14 16 18
# even_numbers = [x for x in range(2, 20, 2)]

even_numbers = [x for x in range(200) if  x % 2 == 0 and x > 0 and x < 20]

print(even_numbers)

# Simil ternario JS
# JS ternario = expresión ? salida true : salida false
conditional = "Existe" if 5 > 6 else "No existe"
print(conditional)

fruits = ['manzana', 'naranja', 'mango']
others = [f for f in fruits if not f.startswith("m")] # 'naranja'

print(others)