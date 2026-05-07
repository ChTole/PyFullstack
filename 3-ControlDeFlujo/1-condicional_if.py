# Pido una edad y evaluo si es mayor de edad (edad >= 18).

print("Comienzo")

age = input("Ingresá tu edad: ")
# input() devuelve 'str' por defecto!!!

# Validar el dato
# Métodos de los str en Python
# https://docs.python.org/es/3/library/stdtypes.html#string-methods
# https://www.w3schools.com/python/python_ref_string.asp

# if expresión (relacional ó lógica):
if age.isdigit(): # devuelve True si la cadena contiene sólo dígitos
    
    # "-55" => isdigit() == False
    # con el indentado o tabulación estoy dentro del condicional
    print("Dato válido!")

    # Casting / Casteo / Conversión
    age = int(age)

    # CONDICIONAL ANIDADO (INDENTADO DENTRO DEL OTRO CONDICIONAL)
    # if - elif - else
    # if age <= 0 or age >= 125:
    if age not in range(1, 126):
        print("La edad ingresada no es válida!!!")
        # ...
    elif age >= 18:
        print("Sos mayor de edad!")
        # ...
    else:
        print("No sos mayor de edad")    
        # ...

# if - else
else:
    print("Dato INVÁLIDO!!!")
    
print("Fin del programa")