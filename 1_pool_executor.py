from concurrent.futures import ProcessPoolExecutor
from time import sleep

def backup_computo(message):
    '''Espera n cantidad de segundos para regresar el mensaje.'''
    print("Creando backup...")
    sleep(10)

    return message

def listar_computos():
    '''Espera 2 segundos para regresar el mensaje.'''
    sleep(5)
    print("Lista de cómputos: ")
    print("Cómputo #1")
    print("Cómputo #2")

def main():
    """Ejecuta las funciones definidas previamente simulando LRO."""

    #El Pool executor está construido con 5 hilos.
    executor = ProcessPoolExecutor(5)
    future = executor.submit(backup_computo, ("Proceso de backup completado."))
    tarea = executor.submit(listar_computos)
    # ¿ya terminó el backup?
    print(future.done())
    sleep(2)
    # Listemos algunos backups mientras se crea el backup que estamos haciendo.
    print(tarea.done())
    # ¿ya terminó el backup?
    print(future.done())
    # Imprime el resultado.
    print(future.result())

if __name__ == '__main__':
    main()

# Nota:
# Todos los LRO'S tiene que tener un ID único.