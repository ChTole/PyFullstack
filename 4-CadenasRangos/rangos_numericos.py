# Función incorporada range()
# Argumentos: siempre números enteros -int-

# Requisito: por lo menos 1 argumento (hasta -exc-)
range_number = range(5) # devuelve: 0, 1, 2, 3, 4 // hasta argumento excluido

print(range_number)
print(range_number[2]) # posición/índice 2 en el rango

other_range = range(5, 10) # devuelve: 5, 6, 7, 8, 9 (desde, hasta -excluido-)

print(other_range)
print(other_range[2])

multiply_3 = range(3, 16, 3) # devuelve: 3, 6, 9, 12, 15 (desde, hasta -exc-, paso)

print(multiply_3)
print(multiply_3[2])

# Por defecto: (desde 0, hasta -exc-, de a 1)