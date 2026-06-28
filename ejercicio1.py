from funciones import (
    agregar_libro, 
    menu_principal, 
    validar_opcion, 
    buscar_libro, 
    eliminar_libro, 
    actualizar_disponibilidad, 
    listar_libros)
    
libros = []


while True:
    opcion = 0
    menu_principal()
    opcion = validar_opcion(opcion)
    if opcion == 1:
        agregar_libro(libros)
    if opcion == 2:
        titulo_buscar    = input("\nIngrese el titulo del libro que desea buscar: ")
        titulo_buscar    = titulo_buscar.strip().lower()
        libro_encontrado = buscar_libro(libros, titulo_buscar)
    if opcion == 3:
       libro_eliminar = input("\nIngrese el titulo del libro que desea eliminar: ")
       libro_eliminar = libro_eliminar.strip().lower()
       libro_eliminado = eliminar_libro(libros, libro_eliminar)
    if opcion == 4:
        actualizar_disponibilidad(libros)
    if opcion == 5:
        listar_libros(libros)
    if opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break
