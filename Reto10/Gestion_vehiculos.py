class vehiculo:
    def __init__(self,marca,modelo,anio):
        self.marca=marca
        self.modelo=modelo
        self.anio=anio

    def descripcion(self):
        return f"Marca: {self.marca}\n Modelo: {self.modelo}\n Anio: {self.anio}"
    

class auto(vehiculo):
    def __init__(self, marca, modelo, anio,num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas=num_puertas
    
    def descripcion(self):
        return f"{super().descripcion()}\n Numero de Puertas: {self.num_puertas}"


class moto(vehiculo):
    def __init__(self, marca, modelo, anio,tipo):
        super().__init__(marca, modelo, anio)
        self.tipo=tipo
    def descripcion(self):
        return f"{super().descripcion()}\n Tipo: {self.tipo}"
