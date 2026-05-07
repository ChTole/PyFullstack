# Estructura repetitiva indefinida/indeterminada

print("*** Comienzo ***")

# Pedir contraseña
user_pass = "123aBc"
# input_pass = input("Ingresá tu contraseña: ")
counter = 0

# while input_pass != user_pass:
while counter < 3:
    input_pass = input("Ingresá tu contraseña: ")
    # el ámbito es el mismo que el del control de flujo
    # user = "Christian"
    
    # anidada por indentado
    if input_pass == user_pass:
        print("Ingreso aceptado!")
        break # Salgo del bucle y no ejecuto "else"
        # print("Ingreso aceptado!") # nunca se ejecuta
    
    counter += 1
# OPCIONALMENTE
else: # cuando la condición del while sea False
    print("Agotaste los intentos para ingresar!!!")
    
# print(user)
print("*** Fin ***")