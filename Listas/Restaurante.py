segunda_es_todo = ["Fritada", "Ceviche de camarón", "Encebollado", "Cuy asado", "Bolón de verde", "Fanesca"]

# Agregar un plato al menú
segunda_es_todo.append(input("1. Agregar un plato al menú: "))

# Buscar un plato en el menú
plato_buscar = input("2. Buscar en el menú: ")
if plato_buscar in segunda_es_todo:
    print(f"El plato '{plato_buscar}' está en la posición {segunda_es_todo.index(plato_buscar)} del menú.")
else:
    print(f"El plato '{plato_buscar}' no se encuentra en el menú.")

# Eliminar un plato del menú
plato_eliminar = input("3. Eliminar un plato del menú: ")
if plato_eliminar in segunda_es_todo:
    segunda_es_todo.remove(plato_eliminar)
else:
    print(f"El plato '{plato_eliminar}' no se encuentra en el menú.")

# Mostrar el menú
print(f"4. Mostrar platos del menu: {segunda_es_todo}")
