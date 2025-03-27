from laptop import laptop

laptop_jefferson=laptop("Acer","Rizen 7",16)
laptop_maria=laptop("HP","Core i7",16,560)
# nueva_laptop=laptop.azuslaptop()

for numero in range(1,10):
    nueva_laptop=laptop.azuslaptop(numero)
    print(nueva_laptop.__dict__)
    

# print(laptop_jefferson.__dict__)
# print(laptop_jefferson.precio_final())
# print(f"El valor de descuento es: {laptop_jefferson.valor_descuento(10)}")
# print(laptop.comparar_costo(laptop_jefferson,laptop_maria))
# print(nueva_laptop.__dict__)