from Libro import libro
from Gestion_vehiculos import vehiculo,auto,moto
from Gestion_empleados import empleado,EmpleadoMedioTiempo,EmpleadoTiempoCompleto

print("## CLASE LIBROS")

libro1=libro("Don Quijote de la Mancha","Miguel de Cervantes",500)
libro2=libro("El señor de los anillos","J.R.R. Tolkien",640)
libro3=libro("La Odisea","Homero",100)

print(libro1.mostrar_info())
print(libro2.mostrar_info())
print(libro3.mostrar_info())

print(f"\n{libro1.titulo} es grande?: {libro.es_grande(libro1.paginas)}")
print(f"{libro2.titulo} es grande? {libro.es_grande(libro2.paginas)}")
print(f"{libro3.titulo} es grande? {libro.es_grande(libro3.paginas)}")

print(libro.total_libros())

print("\n## CLASE VEHICULOS")

auto1 = auto("Toyota", "Corolla", 2022, 4)
moto1 = moto("Honda", "CB500X", 2021, "Adventure")

print(auto1.descripcion())
print(moto1.descripcion())

vehiculos = [auto1, moto1]
print("\nLista de vehículos:")
for vehiculo in vehiculos:
    print(vehiculo.descripcion())


print("\n## CLASE EMPLEADOS")
empleado1=EmpleadoTiempoCompleto("Jefferson Toaquiza",500.25)
empleado2=EmpleadoMedioTiempo("Fernanda Perdomo",600.35)
empleado3=EmpleadoMedioTiempo("Erika Casa",400.35)

print(f"{empleado1.nombre} tiene un sueldo de: {empleado1.calcular_salario()}")
print(f"{empleado2.nombre} tiene un sueldo de : {empleado2.calcular_salario()}")
print(f"{empleado3.nombre} tiene un sueldo de : {empleado3.calcular_salario()}")

empleados=[empleado1,empleado2,empleado3]
print("\n Lista de Empleados: ")
for emplead in empleados:
    print(f"Nombre: {emplead.nombre}, Salario Final: {emplead.calcular_salario()}")