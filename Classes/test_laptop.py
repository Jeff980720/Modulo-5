from laptop import laptop
from laptopgaming import laptop_Gaming
from Laptop_Business import laptop_business

laptop_jefferson=laptop("Acer","Rizen 7",16)
# laptop_maria=laptop("HP","Core i7",16,560)
# # nueva_laptop=laptop.azuslaptop()

# for numero in range(1,10):
#     nueva_laptop=laptop.azuslaptop(numero)
#     print(nueva_laptop.__dict__)
    

# print(laptop_jefferson.__dict__)
# print(laptop_jefferson.precio_final())
# print(f"El valor de descuento es: {laptop_jefferson.valor_descuento(10)}")
# print(laptop.comparar_costo(laptop_jefferson,laptop_maria))
# print(nueva_laptop.__dict__)

laptop_juanito=laptop_Gaming("MSI","i7",4,"RTX 8GB")
# print(laptop_juanito.realizar_diagnostico_sistema())

# laptop_krakedev=laptop_business("MSI","i7",4,"1 TB",5)
# print(laptop_krakedev.realizar_diagnostico_sistema())

def imprimir_funcion(laptop):
    informe = laptop.realizar_informe_uso()
    for clave, valor in informe.items():
        print(f"{clave}:{valor}")
    print("\n")

print("Jefferson: ")
imprimir_funcion(laptop_jefferson)
print("Juanito: ")
imprimir_funcion(laptop_juanito)