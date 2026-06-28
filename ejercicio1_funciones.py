#==============================================================1
def agregar_libro(libros):
    while True:
        titulo = input("\ningrese el titulo del libro: ")
        titulo = titulo.strip().lower()
        if len(titulo.strip().lower()) <= 0:
            print("El titulo del libro no puede estar vacio: ")
        elif titulo.strip().lower() == "":
            print("El titulo del libro no puede estar vacio: ")
        else:
            break
    while True:
        try:
            copias = int(input("\nIngrese la cantidad de copias del libro: "))
            if copias < 0:
                print("\nLa cantidad de libros debe ser un numero entero positivo: ")
        except ValueError:
            print("\n Porfavor ingrese un numero entero positivo: ")
        else:
            break
    while True:
        try:
            prestamo = int(input("\nIngrese el periodo de prestamo del libro: "))
            if prestamo <=0:
                print("\nEl periodo de prestamo no puede ser un numero menor o igual a cero: ")    
        except ValueError:
            print("\nPorfavor ingrese un numero entero positivo: ")
        else:
            print
            break

    libro  = {
    "titulo": titulo,
    "copias": copias,
    "prestamo": prestamo,
    "disponible": ""}
    libros.append(libro)
    return titulo, copias, prestamo, libro["disponible"]
#==============================================================2
def buscar_libro(libros, titulo_buscar):
    encontrado = False
    for libro_encontrado in libros:
        if libro_encontrado["titulo"] == titulo_buscar.strip().lower():
            print(f"Nombre del libro: {libro_encontrado["titulo"]}")
            print(f"Copias : {libro_encontrado["copias"]}")
            print(f"prestamo: {libro_encontrado["prestamo"]}")
            print(f"Estado: {libro_encontrado["disponible"]}")
            encontrado = True
            break
    if not encontrado:
        print("Libro no encontrado.")
                
#==============================================================3

def eliminar_libro(libros, libro_eliminar):
    encontrado = False
    for libro_eliminado in libros:
        if libro_eliminado["titulo"] == libro_eliminar.strip().lower():
           libros.remove(libro_eliminado)
           print(f"El libro '{libro_eliminado["titulo"]}' ha sido eliminado correctamente.")
           encontrado = True
           break
    if not encontrado:
        print(f"El libro {libro_eliminar} no se encuentra registrado.")
    return libros

#==============================================================4
def actualizar_disponibilidad(libros):
    for libro in libros:
        if libro["copias"] > 0:
            libro["disponible"] = "Disponible"
        else:
            libro["disponible"] = "Sin copias"
    print("\nDisponibilidad de libros actualizada correctamente.")
    
#==============================================================5
def listar_libros(libros):
    if not libros:
        print("Aun no hay libros registrados")
    else:
        print("\n===LISTA DE LIBROS===")
        for libro in libros:
            print(f"Titulo: {libro["titulo"]}")
            print(f"Copias: {libro["copias"]}")
            print(f"Prestamo: {libro["prestamo"]}")
            print(f"Estado: {libro["disponible"]}")
            print("***************************************")
#==============================================================
def menu_principal():   
        print("\n====MENU PRINCIPAL====")
        print("1.Agregar libro")
        print("2.Buscar libro")
        print("3.Eliminar libro")
        print("4.Actualizar disponibilidad")
        print("5.Mostrar libros")
        print("6.Salir")
    

#==============================================================
def validar_opcion(opcion):
    while True:
        opcion = int(input("Ingrese una opcion: "))
        try:
            if opcion <= 0 or opcion > 6:
                print(" Opcion invalida, ingresa una opcion valida")
            else:
                return opcion
        except ValueError:
            print(" Opcion invalida, ingresa una opcion valida")
