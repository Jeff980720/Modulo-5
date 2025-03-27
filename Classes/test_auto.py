from auto import auto

auto_jefferson=auto("Toyota","Corolla",2020)
auto_jose=auto("Toyota","Rush",2020,5000)

# print(f"Informacion del auto inicial: ")
# auto_jefferson.mostrar_informacion()
# print(f"El kilometraje ahora es de: {auto_jefferson.actualizar_kilometraje(1000)}")
# auto_jefferson.mostrar_informacion()
# print(f"Informacion de kilometros recorridos del auto tras los viajes {auto_jefferson.realizar_viaje()}")
# auto_jefferson.estado_auto()
# print("Informacion del auto final: ")
# auto_jefferson.mostrar_informacion()

print(auto.comparar_kilometraje(auto_jefferson,auto_jose))

for numero in range(1,11):
    nuev_auto=auto.toyota_auto()
    print(nuev_auto.__dict__)

nuev_kilometraje=auto.aumentar_kilom(10000)
print("El kilometraje nuevo es: ",nuev_kilometraje)

# Creo un auto usado
mi_auto_usado = auto.auto_usado("Toyota", "Corolla", 2015, 85000)
print(f"Auto: {mi_auto_usado.marca} {mi_auto_usado.modelo}, Año: {mi_auto_usado.anio}, Kilometraje: {mi_auto_usado.kilometraje}")

