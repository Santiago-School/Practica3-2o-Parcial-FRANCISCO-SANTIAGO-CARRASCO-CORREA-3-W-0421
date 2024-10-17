print("Francisco Santiago Carrasco Correa 0421 3°W")
print(" ")
# diccionario vacio para almacenar palabras junto con sus definiciones
diccionariopalabras = {}

def agregarentrada():
    """
    solicita al usuario ingresar una palabra y su definicion.
    la palabra se almacena en el diccionario con la definicion proporcionada.
    """
    palabra = input("por favor, ingresa la palabra: ").lower()
    definicion = input("ahora, ingresa la definicion de la palabra: ")
    diccionariopalabras[palabra] = definicion
    print(f"la palabra '{palabra}' se ha agregado exitosamente al diccionario.")

def buscardefinicion():
    """
    permite al usuario buscar la definicion de una palabra.
    si la palabra esta en el diccionario, muestra la definicion.
    si no, informa al usuario que la palabra no existe en el diccionario.
    """
    palabra = input("introduce la palabra que deseas buscar: ").lower()
    if palabra in diccionariopalabras:
        print(f"la definicion de '{palabra}' es: {diccionariopalabras[palabra]}")
    else:
        print(f"la palabra '{palabra}' no se encuentra en el diccionario.")

def mostrardiccionario():
    """
    muestra todas las palabras y sus definiciones almacenadas en el diccionario.
    si el diccionario esta vacio, muestra un mensaje informando de ello.
    """
    if diccionariopalabras:
        print("\n--- diccionario actual ---")
        for palabra, definicion in diccionariopalabras.items():
            print(f"{palabra.capitalize()}: {definicion}")
    else:
        print("el diccionario esta vacio. aun no has agregado ninguna palabra.")

def menuprincipal():
    """
    muestra el menu principal con opciones para interactuar con el diccionario.
    el menu permite agregar palabras, buscar definiciones, visualizar el diccionario completo o salir del programa.
    """
    while True:
        print("\n--- menu principal ---")
        print("1. agregar una nueva palabra")
        print("2. buscar definicion de una palabra")
        print("3. ver el diccionario completo")
        print("4. salir del programa")

        opcion = input("selecciona una opcion (1-4): ")

        if opcion == '1':
            agregarentrada()
        elif opcion == '2':
            buscardefinicion()
        elif opcion == '3':
            mostrardiccionario()
        elif opcion == '4':
            print("¡gracias por usar el diccionario! hasta luego.")
            break
        else:
            print("opcion invalida, por favor selecciona una opcion valida (1-4).")

# ejecutar el menu principal para iniciar la aplicacion
menuprincipal()
