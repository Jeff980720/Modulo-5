import random

viaje=int(input("¿A qué país deseas viajar, ingresa el codigo internacional? (Ecuador: 593, Colombia: 57, Peru; 51): "))

ecuador=random.randint(1, 200)
colombia=random.randint(1, 200)
peru=random.randint(1, 200)

if viaje==593:
    if ecuador>=10 and ecuador<=40:
        print("Viajando en Ecuador")
        print(f"La velicidad es de: {ecuador} km/h")
        print("Nos encontramos en Zona Urbana")
    elif ecuador>=41 and ecuador<=60:
        print("Viajando en Ecuador")
        print(f"La velicidad es de: {ecuador} km/h")
        print("Nos encontramos en Zona Rural")
    elif ecuador>=61 and ecuador<=120:
        print("Viajando en Ecuador")
        print(f"La velicidad es de: {ecuador} km/h")
        print("Nos encontramos en Zona Perimetral")
    elif ecuador<10:
        print("Viajando en Ecuador")
        print(f"La velicidad es de: {ecuador} km/h")
        print("El limite de velocidad minimo es de 10 km/h por favor aumente la velocidad")
    elif ecuador>120:
        print("Viajando en Ecuador")
        print(f"La velicidad es de: {ecuador} km/h")
        print("El limite de velocidad maximo es de 120 km/h por favor disminuya la velocidad")

elif viaje==57:
    if colombia>=10 and colombia<=30:
        print("Viajando en Colombia")
        print(f"La velicidad es de: {colombia} km/h")
        print("Nos encontramos en Zona Urbana")
    elif colombia>=31 and colombia<=80:
        print("Viajando en Colombia")
        print(f"La velicidad es de: {colombia} km/h")
        print("Nos encontramos en Zona Rural")
    elif colombia>=81 and colombia<=100:
        print("Viajando en Colombia")
        print(f"La velicidad es de: {colombia} km/h")
        print("Nos encontramos en Zona Perimetral")
    elif colombia<10:
        print("Viajando en Colombia")
        print(f"La velicidad es de: {colombia} km/h")
        print("El limite de velocidad minimo es de 10 km/h por favor aumente la velocidad")
    elif colombia>100:
        print("Viajando en Colombia")
        print(f"La velicidad es de: {colombia} km/h")
        print("El limite de velocidad maximo es de 100 km/h por favor disminuya la velocidad")

elif viaje==51:
    if peru>=10 and peru<=40:
        print("Viajando en Peru")
        print(f"La velicidad es de: {peru} km/h")
        print("Nos encontramos en Zona Urbana")
    elif peru>=41 and peru<=60:
        print("Viajando en Peru")
        print(f"La velicidad es de: {peru} km/h")
        print("Nos encontramos en Zona Rural")
    elif peru>=61 and peru<=120:
        print("Viajando en Peru")
        print(f"La velicidad es de: {peru} km/h")
        print("Nos encontramos en Zona Perimetral")
    elif peru<10:
        print("Viajando en Peru")
        print(f"La velicidad es de: {peru} km/h")
        print("El limite de velocidad minimo es de 10 km/h por favor aumente la velocidad")
    elif peru>120:
        print("Viajando en Peru")
        print(f"La velicidad es de: {peru} km/h")
        print("El limite de velocidad maximo es de 120 km/h por favor disminuya la velocidad")
else:
    print("Ingrese un codigo valido")
