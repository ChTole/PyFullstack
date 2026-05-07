# Operadores de asignación compuestos
number = 5
# number = number + 1
number += 1 # para la suma
print("Mi número = ", number) # (variable, expresion, dato, ...)
number *= 2
print("Mi número = ", number)
number **=3
print("Mi número = ", number)


# Operador de pertenencia
# Evalua la pertenencia dentro de una colección (*ampliaremos)
word = "abracadabra"
print("Pertenencia de a: ", "a" in word)
print("Pertenencia de z: ", "z" in word)


# Operador de identidad
is_true = True # Guardo un booleano en memoria
copy_is_true = is_true # Es una REFERENCIA y no UNA COPIA

print("Identidad", copy_is_true is is_true)
print("Valor original: ", is_true)
print("Copiado (?): ", copy_is_true)

is_true = False
print("Identidad", copy_is_true is is_true)
print("Valor original: ", is_true)
print("Copiado (?): ", copy_is_true)