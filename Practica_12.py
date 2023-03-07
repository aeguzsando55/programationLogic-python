import math

''' 
    While loop (Bucle Mientras)
    La sentencia (hacer mientras) crea un bucle que ejecuta una sentencia especificada, 
    hasta que la condición de comprobación se evalúa como falsa. La condición se evalúa 
    después de ejecutar la sentencia, dando como resultado que la sentencia especificada 
    se ejecute al menos una vez.
'''

# * Proceso


def imprimirNumeros(n):
    """ Imprime los primeros números deseados, tomando como argumento la varable entera n.

    Args:
        n (int): n números que se desean imprimir uno a uno.
    """
    i = 0
    while (i < abs(n)):
        print(i+1)
        i += 1


def sumarNumeros(n):
    """Realiza una suma de los primeros numeros deseados, tomando n como argumento único

    Args:
        n (int): n numeros iniciales.

    Returns:
        suma (int): La suma de los n números.
    """
    i = 1
    suma = 0
    while (i <= abs(n)):
        suma += i
        i += 1
    return suma


def coincidirNumeros(a, b):
    while (a != b):
        print(f'los numeros {a} y  {b} no son iguales... Vuelva a intentart')
        a = int(input('a..: '))
        b = int(input('a..: '))
    print(f'Los numeros {a} y {b} son iguales')


if __name__ == '__main__':
    # * 1. imprimiremos los primeros n numeros deseados:
    n = int(input("Cuantos números desea imprimir...: "))
    imprimirNumeros(n)

    # * 2. Ahora sumamos los numeros
    print(f'La suma de los primeros {n} numeros es igual a {sumarNumeros(n)}')

    # * 3. Concidir numeros
    a = int(input("Ingrese el primer numero...: "))
    b = int(input("Ingrese el segundo numero...: "))
    coincidirNumeros(a, b)
