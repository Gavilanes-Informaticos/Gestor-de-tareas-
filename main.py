from Agregar import agregar_tarea
from eliminar import eliminar_tarea
from mostar import mostrar_tareas
from editar import editar_tarea

def mostrar_menu():
    """Imprime en pantalla las opciones del menú."""
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Salir")

def menu():
    """
    Controlador principal del programa. 
    Mantiene la lista de tareas y maneja las entradas del usuario.
    """
    lista_tareas = []
    
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ")
        
        if opcion == '1':
            nueva_tarea = input("Ingresa la nueva tarea: ")
            agregar_tarea(lista_tareas, nueva_tarea)
            
        elif opcion == '2':
            mostrar_tareas(lista_tareas)
            
        elif opcion == '3':
            mostrar_tareas(lista_tareas)
            try:
                indice = int(input("Ingresa el número de la tarea a editar: "))
                nueva_desc = input("Ingresa la nueva descripción: ")
                editar_tarea(lista_tareas, indice, nueva_desc)
            except ValueError:
                print("Error: Por favor, ingresa un número entero válido.")
                
        elif opcion == '4':
            mostrar_tareas(lista_tareas)
            try:
                indice = int(input("Ingresa el número de la tarea a eliminar: "))
                eliminar_tarea(lista_tareas, indice)
            except ValueError:
                print("Error: Por favor, ingresa un número entero válido.")
                
        elif opcion == '5':
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
