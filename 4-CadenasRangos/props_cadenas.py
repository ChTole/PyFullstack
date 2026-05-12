# Características de las cadenas en Python

# Los caracteres tienen índices
word = "aeropuerto"
#       0123456789

print(word[0]) # entre corchetes indico el índice a acceder
print(word[8])

# "Slice" o rebanadas

print(word[0:4]) # [desde: hasta-excluido-]

print(word[0:9:2]) # [desde: hasta-excluido-: paso]

print(word[-1]) # último caracter

print(word[-1::-1]) # [último:principio:hacia atrás]

# Por defecto [principio:fin:de a 1]

country = "Argentina"

print(f"Abrev: {country[:3].upper()} - País: {country}")