def editar_tarea(lista_tareas, indice, nueva_descripcion):
    """
    Actualiza la descripción de una tarea basándose en su índice.
    Valida que el índice exista y que el nuevo texto no esté vacío.
    """
    if 0 <= indice < len(lista_tareas):
        if nueva_descripcion.strip():
            tarea_anterior = lista_tareas[indice]
            lista_tareas[indice] = nueva_descripcion
            print(f"Tarea '{tarea_anterior}' editada a '{nueva_descripcion}' con éxito.")
        else:
            print("Error: La nueva descripción de la tarea no puede estar vacía.")
    else:
        print("Error: El índice proporcionado no es válido.")
