import random

from laptop import laptop

class laptop_business(laptop):
    def __init__(self, marca, procesador, memoria,espacio_disco,duracion_bateria, costo=500, impuesto=10):
      super().__init__(marca, procesador, memoria, costo, impuesto)
      self.espacio_disco = espacio_disco
      self.duracion_bateria = duracion_bateria
    
    def realizar_diagnostico_sistema(self):
       result_diag= super().realizar_diagnostico_sistema()
       result_conect=self.verificar_conectividad_red()
       result_diag["Conectividad del equipo"]=result_conect
       return result_diag
    
    def verificar_conectividad_red(self):
       resultado={
          "Wi-Fi":"Conectado" if random.choice([True,False]) else "Sin Conexion Inalambrica",
          "Servidor Empresarial":"Posee Servidor" if random.choice([True,False]) else "Sin Servidos",
          "Latencia de Red":"Alta latencia" if random.choice([True,False]) else "Baja latencia"
       }
       return resultado