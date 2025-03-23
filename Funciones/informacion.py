from datetime import datetime

nombre_paciente=[]
edad=[]

def agregar_nombre(nombre,apellido):
    nombre_completo = nombre + " " + apellido
    nombre_paciente.append(nombre_completo)
    print(f"Nombre agregado con éxito")
    

def agregar_edad(edad_nacimiento):
    edad_actual = datetime.now().year - edad_nacimiento
    edad.append(edad_actual)
    print(f"Edad agregada con éxito")


def mostrar():
    combinado = list(zip(nombre_paciente,edad))
    mayor = max(combinado, key=lambda x: x[1])
    menor= min(combinado, key=lambda x: x[1])
    print(f"Lista de nombres: {nombre_paciente}")
    print(f"Lista de edades: {edad}")
    print(f"{mayor[0]} con la edad de {mayor[1]} años es mayor a los demás pacientes.")
    print(f"{menor[0]} con la edad de {menor[1]} años es menor a los demás pacientes.")
