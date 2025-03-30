import random

class laptop:
    def __init__(self, marca, procesador, memoria, costo=500,impuesto=10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def precio_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo - descuento)/100

    def realizar_diagnostico_sistema(self):
        resultado={
            "MARCA":f"{self.marca}",
            "PROCESADOR":f"{self.procesador}",
            "MEMORIA RAM":"OK" if self.memoria>=8 else "AUMENTAR MEMORIA RAM",
            # "Disco Duro":self.espacio_disco,
            # "Duracion de bateria":f"{self.duracion_bateria} HORAS",
            "BATERIA":"OK" if random.choice([True,False]) else "CAMBIA DE BATERIA"
        }
        return resultado
    
    def realizar_informe_uso(self):
        resultado_informe={
            "Tipo":"Generica",
            "Uso recomendado":"Tareas cotidianas",
            "Horas de uso":5,
            "Diagnostico actual":self.realizar_diagnostico_sistema()
        }
        return resultado_informe

    @staticmethod
    def comparar_costo(laptop1,laptop2):
        if laptop1.costo==laptop2.costo:
            return "Los costos son iguales"
        return "Los costos son diferentes"
    
    @classmethod
    def azuslaptop(cls,costo):
        marca="Azus"
        procesador="i5"
        memoria=16
        return cls(marca,procesador,memoria,costo)

        