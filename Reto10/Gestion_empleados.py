from abc import ABC,abstractmethod

class empleado(ABC):
    def __init__(self,nombre,salario_base):
        self.nombre=nombre
        self.salario_base=salario_base
    
    @abstractmethod
    def calcular_salario(self):
        pass

class EmpleadoTiempoCompleto(empleado):
    def calcular_salario(self):
        return round(self.salario_base*1.2,2)

class EmpleadoMedioTiempo(empleado):
    def calcular_salario(self):
        return round(self.salario_base*1.1,2)
