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

laptop_jefferson=laptop("Acer","Rizen 7",16)

print(laptop_jefferson.__dict__)
print(laptop_jefferson.precio_final())
print(f"El valor de descuento es: {laptop_jefferson.valor_descuento(10)}")

        