def agregar_tarea(lista_tareas, nueva_tarea):
    """Agrega una nueva tarea a la lista si no está vacía."""
    if nueva_tarea.strip():
        lista_tareas.append(nueva_tarea)
        print(f"✔ Tarea '{nueva_tarea}' añadida con éxito.")
    else:
        print("La tarea no puede estar vacía.")
