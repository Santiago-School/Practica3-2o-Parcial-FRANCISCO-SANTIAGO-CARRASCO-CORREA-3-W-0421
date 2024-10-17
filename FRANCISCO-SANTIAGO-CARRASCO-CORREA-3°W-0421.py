print("Francisco Santiago Carrasco Correa 0421 3°W ")
# 1 diccionario de divisas
divisas = {'euro': '€', 'dolar': '$', 'yen': '¥'}

# solicitar al usuario una divisa
divisausuario = input("introduce una divisa (euro, dolar, yen): ").lower()

# mostrar el simbolo o un mensaje de error
if divisausuario in divisas:
    print(f"el simbolo de {divisausuario} es {divisas[divisausuario]}")
else:
    print("la divisa no está en el diccionario")
