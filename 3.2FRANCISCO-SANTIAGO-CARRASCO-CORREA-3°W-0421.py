print("Francisco Santiago Carrasco Correa 0421 3°W ")
print(" ")
#  diccionario con datos del usuario
usuario = {}

# solicitar datos al usuario
usuario['nombre'] = input("introduce tu nombre: ")
usuario['edad'] = input("introduce tu edad: ")
usuario['direccion'] = input("introduce tu direccion: ")
usuario['telefono'] = input("introduce tu teléfono: ")

# mostrar los datos del usuario
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su numero de telefono es {usuario['telefono']}")
