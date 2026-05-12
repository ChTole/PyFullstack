# Estructura repetitiva determinada o definida
# Recorre iterables

word = "aeropuerto"
multiply_3 = range(3, 16, 3) # 3, 6, 9, 12, 15


# Sintaxis: for <variable_aux> in <iterable>:
for letter in word: # a - e - r ...
    print("Letra:", letter, " - índice: ", word.index(letter))
    
    
for n in multiply_3: # 3...15
    print(f"Número: {n}")
    # print(word[n]) # IndexError: string index out of range


# OPCIONALES
for n in multiply_3: # 3, 6, 9, 12, 15 
    
    if n % 6 == 0:
        continue # vuelve al principio, pasa al siguiente valor
        
    # "Rompo" el bucle
    if n % 12 == 0:
        break
    
    print(f"n vale = {n} ") # "n vale 3"
else: # se ejecuta cuando termina el bucle sin break
    print("Se recorrieron todos los valores")
    
# fuera del bucle
print("Fin del programa.")