from concurrent.futures import ProcessPoolExecutor
from time import sleep

def task(message):
    '''Espera 2 segundos para regresar el mensaje.'''
    
    sleep(2)
    return message

def main():
    """Ejecuta la función para arrojar el mensaje con delay de 2 segundos."""

    #El Pool executor está construido con 5 hilos
    executor = ProcessPoolExecutor(5)
    future = executor.submit(task, ("Completed"))
    print(future.done())
    sleep(2)
    print(future.done())
    print(future.result())

if __name__ == '__main__':
    main()