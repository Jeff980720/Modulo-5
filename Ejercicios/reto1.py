#Reto calculadora

alto=float(input("Ingresar el alto del rectangulo: "))
ancho=float(input("Ingresar el ancho del rectangulo: "))

area=alto*ancho
perimetro=2*(alto+ancho)
superficie=area+perimetro

print(f"El área del rectangulo es: {area} m2")
print(f"El perímetro del rectangulo es: {perimetro} m")     
print(f"La superficie del rectangulo es: {superficie} m2")