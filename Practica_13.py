'''
    Calculo de potencia, factoriales y serie Fibonacci
    
    Continuando con el bucle while, implementaremos las secuencias de una serie fbonacci, el calculo 
    del factorial de un numero N (N!) y la potencia de un número. Observaremos como es posble la 
    implementacion de estas funciones con la ayuda de un bucle while.
    
    La función factorial se representa con un signo de exclamación “!” detrás de un número. Esta exclamación 
    quiere decir que hay que multiplicar todos los números enteros positivos que hay entre ese número y el 1. 
    A este número, N! le llamamos generalmente “N factorial”, aunque también es correcto decir “factorial de N”.
    
    La suceción o serie Fibonacci es una secuencia infinita de números naturales; a partir del 0 y el 1, se van 
    sumando a pares, de manera que cada número es igual a la suma de sus dos anteriores, de manera que: 
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55… 
'''

def potencia(a, N):  
    i = 0 # Contador
    aPot = 1 # variable auxilar para ncrementar el exponente
    while(i < N): # Suponiendo que N = 2
        aPot = aPot * a  # Suponiendo que a = 5 en la primera vuelta aPot = 1 * 5 = 5
        i += 1 # Incrementamos el contador
    return aPot # Al final aPot = 5 * 5 = 25

def factorial(N):
    nFact = 1 # Variable auxiliar para acumular el producto de los numeros 
    i = 1 
    while (i < N): # Suponiendo que N = 5
        nFact = nFact * (i + 1) # En la primera vuelta nFact = 1 * (1 + 1) = 1 * 2 = 2 
        i += 1
    return nFact # Al final nFact = 24 * 5 = 120

def fibonacci(N):
    fib = 0 # Variable auxiliar para alamacenar la sucecion de numeros
    a = 0 # primer termino
    b = 1 # segundo termino

    while(fib < N):
        fib = a + b # Suma los terminos, en la siguiente vuelta se reinicia con terminos actualizados
        print(f'{a} + {b} = {fib}')
        a = b # el primer termino toma el valor del segundo
        b = fib # el segundo termino toma el valor de la suma de los terminos



if __name__ == '__main__':
    
    print('Calular a a la N potencia')
    # a = int(input('Ingresa un número...: '))
    # N = abs(int(input('Ingresa la potencia...: ')))
    a = 5
    N = 2
    print(f'{a}^{N} = {potencia(a, N)}')
    
    print('Calcular N factorial')
    # N = abs(int(input('Ingrese un número entero positivo...: ')))
    N = 5
    print(f'{N}! = {factorial(N)}')
    
    N = 21
    print(f'Calculo de los primeros {N} terminos de la serie Fibonacci')
    fibonacci(N)
    