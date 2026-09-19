def eliminar_tarea(lista_tareas, indice):
    if 0 <= indice < len(lista_tareas):
        eliminada = lista_tareas.pop(indice)
        print(f"✔ Tarea eliminada: '{eliminada}'")
    else:
        print("❌ Índice no válido o lista vacía")