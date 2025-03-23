import random

aleatorio=random.randint(1, 9)
aleatorio_dos=random.randint(1, 9)

print(f"El primer número es:  {aleatorio} y el segundo número es: {aleatorio_dos}")

if aleatorio==4:
    print("Te ganaste un chupete")
elif aleatorio==7 and aleatorio_dos==3:
    print("Te ganaste un carro")
elif aleatorio==2:
    print("Te ganaste una moto")
else:
    print("No te ganaste nada")