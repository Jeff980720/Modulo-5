from laptop import laptop

class laptop_Gaming(laptop):
    def __init__(self, marca, procesador, memoria,tarjt_grafica, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tart_grafica=tarjt_grafica

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico= super().realizar_diagnostico_sistema()
        resultado_juegos=self.realizar_diagnostico_juegos()
        resultado_diagnostico["Resultado Juegos"]=resultado_juegos
        return resultado_diagnostico
    
    def realizar_diagnostico_juegos(self):
        juegos=["FORNITE","COD","GTA"]
        resultados={}
        for juego in juegos:
            fps_base=30
            if "RTX" in self.tart_grafica:
                fps=fps_base*3
            elif "GTX" in self.tart_grafica:
                fps=fps_base*2
            else:
                fps=fps_base
            resultados[juego]=f"{fps} FPS"
        return resultados
    pass