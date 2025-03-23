class auto:
    def __init__(self,marca,modelo,anio,kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_informacion(self):
        return print(auto_jefferson.__dict__)
    
    def actualizar_kilometraje(self,nuevo_kilometraje):
        if nuevo_kilometraje <= self.kilometraje:
            print("No puedes disminuir el kilometraje")
        else:
            self.kilometraje = nuevo_kilometraje
            return self.kilometraje
    
    def realizar_viaje(self):
        viajes=int(input("Ingrese la cantidad de viajes que desea realizar: "))
        for i in range(viajes):
            print(f"Viaje {i+1}")
            distancia = int(input("Ingrese la cantidad de kilometros recorridos: "))

            if distancia < 0:
                print("La cantidad de kilometros no puede ser negativa")
            else: 
                self.kilometraje = auto_jefferson.kilometraje + distancia
        return self.kilometraje
        
    def estado_auto(self):
        if self.kilometraje<20000:
            print("Estado el auto: Estoy como nuevo")
        elif 20000<=self.kilometraje<100000:
            print("Estado el auto: Ya estoy usado")
        else:
            print("Estado el auto: Ya dejame dsecansar por favor") 

auto_jefferson=auto("Toyota","Corolla",2020)

print(f"Informacion del auto inicial: ")
auto_jefferson.mostrar_informacion()
print(f"El kilometraje ahora es de: {auto_jefferson.actualizar_kilometraje(1000)}")
auto_jefferson.mostrar_informacion()
print(f"Informacion de kilometros recorridos del auto tras los viajes {auto_jefferson.realizar_viaje()}")
auto_jefferson.estado_auto()
print("Informacion del auto final: ")
auto_jefferson.mostrar_informacion()