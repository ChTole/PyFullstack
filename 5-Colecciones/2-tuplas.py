# Estructura de datos II
# Tuplas - tuple()
# Documentación:
# https://docs.python.org/es/3.14/tutorial/datastructures.html#tuples-and-sequences
# https://www.w3schools.com/python/python_tuples.asp

# Formas de creación
# 1- Elementos separados por comas y entre paréntesis
days = ('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes')
# 2- Elementos separados por comas
days = 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'

print("Días: ", days)
print("Tipo: ", type(days))
print("Primer día hábil: ", days[0])

print('*' * 30)
one_element = 3.14, # SI TIENE UN SÓLO ELEMENTO, DEBE TENER COMA AL FINAL

print(one_element)
print(type(one_element))

print('*' * 30)
other_tuple = ('Chris', 45, 1.7, False, False, ('Leia', 'Naranjo'), [0, 1, 2])
print(other_tuple)

# other_tuple.append(3.14) # AttributeError: 'tuple' object has no attribute 'append'
other_tuple[6].append(3)
print(other_tuple)

copy_tuple = list(other_tuple)
print(copy_tuple)
print(type(copy_tuple))

print('*' * 30)
for element in other_tuple:
    print("Dato: ", element)
    # print(type(element))
    
    if type(element) == list:
        print("Es mutable")
    


# Propiedades:
# - Son ordenadas porque tienen índices.
# - Son heterogeneas porque aceptan distintos tipos de datos.
# - Son inmutables porque NO puedo agregar o quitar elementos.
# - Admiten datos repetidos.

