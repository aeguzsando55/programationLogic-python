'''
    For Loop (Bucle Para)
    
    Un bucle for es una estructura de programación que permite repetir un bloque de código varias veces 
    utilizando una variable de control (i). Se inicia con un valor (i = 0), se comprueba una condición 
    (i < N, donde N es el rango), y se actualiza la variable (i =  i + 1) en cada iteración hasta que la 
    condición no se cumpla más. Es útil para procesar grandes cantidades de datos y automatizar tareas 
    repetitivas.
    
'''

def letterLoop(phrase):
    """
    Prints each letter in a given phrase on a new line.

    Args:
        phrase (str): The phrase to print the letters of.
    """
    for letter in phrase:
        print(letter) # print each letter on a new line

def wordLoop(phrase):
    """
    Prints each word in a given phrase on a new line.

    Args:
        phrase (str): The phrase to print the words of.
    """
    words = phrase.split() # split the phrase into a list of words
    for word in words:
        print(word) # print each word on a new line
        
def printNumbers(N):
    """
    Prints the numbers from 0 to N on a single line, separated by a space character.

    Args:
        N (int): The upper limit of the range of numbers to print.
    """
    for i in range (N):
        print(i, end=' ') # print each number followed by a space character
    print(' ')   # print a newline character at the end of the line 
    
def fibonacci(N):
    """
    Prints the first N terms of the Fibonacci sequence, along with their sum.

    Args:
        N (int): The number of terms to print.
    """
    # initialize variables
    summation, a, b, c = 3, 0, 1, 2
    d = 0
    print(f'{a} + {b} +', end=' ')

    # iterate over remaining terms of the sequence
    for i in range(4, N):
        d = a + b + c  # calculate next term of the sequence
        print(f'{c} + ', end=' ')  # print the current term of the sequence
        summation += d  # update the sum of the sequence
        a, b, c = b, c, d  # update variables for the next iteration

    print('...')  # print ellipsis to indicate sequence continues

if __name__ == '__main__':
    phrase = 'Hello World!'
    
    letterLoop(phrase)
    wordLoop(phrase)

    N = 10
    
    printNumbers(N)
    
    fibonacci(N)