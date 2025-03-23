# Crear una lista llamada datos.
datos = ["Krakedev"]

# el usuario elija ingresar cualquier cantidad de datos
cantidad = int(input("¿Cuántos datos quieres ingresar?: "))

# Debe validar el tipo de dato numérico y guardarlo en una lista llamada datos.
# Para ello se debe investigar un método que permita validar, si en los caracteres existen valores numéricos.
# Validar si es decimal y guardar en la lista datos.
# Validar si es string y guardar en la lista datos.
for i in range(cantidad):
    dato = input(f"Ingrese el dato {i + 1}: ")
    
    # Validamos si el dato es numérico
    if dato.isdigit():  # Verifica si es un número entero
        datos.append(int(dato))  # Lo guarda como un entero
    elif dato.replace('.', '', 1).isdigit() and dato.count('.') < 2:  # Verifica si es un decimal
        datos.append(float(dato))  # Lo guarda como un flotante
    else:
        # Si no es numérico, lo guardamos como un string
        datos.append(dato)

# Imprimir la lista con el siguiente formato:
# f”Su lista es: <datos>”
print(f"Su lista es: {datos}")