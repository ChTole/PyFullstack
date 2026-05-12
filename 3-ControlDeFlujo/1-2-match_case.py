# Estructura match-case (similar switch-case)
# origen: Python 3.10 (año 2023)
# Python NO ES RETROCOMPATIBLE!!!

main_menu = """
*** Menú principal *** 
1- Crear
2- Leer
3- Actualizar
4- Eliminar
5- Salir
"""

print(main_menu)

option = input("Seleccioná una opción >>> ") # DEVUELVE str

# if option == "1":
#     print("Opción 'Crear' en desarrollo")
# elif option == "2":
#     print("Opción 'Leer' en desarrollo")
# elif option == "3":
#     print("Opción 'Actualizar' en desarrollo")
# elif option == "4":
#     print("Opción 'Eliminar' en desarrollo")
# elif option == "5":
#     print("Gracias por usar la app!!! Hasta pronto!")
# else:
#     print("Opción inválida!")

match option: # siempre evalúa un valor, no una expresión
    case "1":
        print("Opción 'Crear' en desarrollo")
    case "2":
        print("Opción Leer' en desarrollo")
    case "3":
        print("Opción 'Actualizar' en desarrollo")
    case "4":
        print("Opción 'Eliminar' en desarrollo")
    case "5":
        print("Adios! Gracias por usar la app!")
    case _:
    # other: # es lo mismo que case _:
        print("Opción inválida!")