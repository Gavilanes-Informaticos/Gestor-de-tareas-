def mostrar_tareas(lista_tareas):
    if len(lista_tareas) == 0:
        print("No hay tareas pendientes")
    else:
        print("Lista de Tareas pendientes:")

        for i in range(len(lista_tareas)):
            print(i, ".", lista_tareas[i])