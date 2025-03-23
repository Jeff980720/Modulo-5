import emoji

cantidad_frases = int(input("¿Cuántas frases deseas ingresar? "))
for i in range(cantidad_frases ):
    frase = input(f"Ingresa una frase {i+1}: ")
    emoji.encontrar_palabra(frase)
    emoji.agregar_frase(frase)