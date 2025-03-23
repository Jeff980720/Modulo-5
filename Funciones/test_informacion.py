import informacion

cantidad_paciente = int(input("¿Cuántos pacientes deseas ingresar?: "))
for i in range(cantidad_paciente):
    print(f"Paciente {i+1}")
    nom = input("Ingrese el nombre: ")
    ape = input("Ingrese el apellido: ")
    edad = int(input("Ingrese el año de nacimiento: "))
    informacion.agregar_nombre(nom, ape)
    informacion.agregar_edad(edad)

informacion.mostrar()