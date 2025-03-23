#Listas

planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
# print(planetas[-6])
# print(planetas[2:])
# print(len(planetas))
# print(planetas[8])

#TRABAJANDO CON LISTAS DE NÚMEROS
gravedad_planetas = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
peso_bus=124054 #Newtons en la tierra

print(f"En la tierra un bus de dos pisos pesa : {peso_bus} N")
print(f"En Mercurio un bus de dos pisos pesa : {peso_bus*gravedad_planetas[0]} N")
print(f"Lo mas liviano que seria un bus en el sistema solar es: {peso_bus*min(gravedad_planetas)} N")
print(f"Lo mas pesado que seria un bus en el sistema solar es: {peso_bus*max(gravedad_planetas)} N")

