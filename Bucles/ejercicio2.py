frase=input("Ingrese una frase: ")
letra=input("Ingrese una letra: ")
contador=0
for i in frase:
    if i==letra:
        contador+=1

print(f"La letra {letra} se repite {contador} veces en la frase")
print(frase.count(letra)) #Otra forma de hacerlo