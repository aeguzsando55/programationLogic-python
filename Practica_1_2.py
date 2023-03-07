import math
import cmath

'''
    Calculo de la formula general para ecuaciones cuadraticas.
    
    La fórmula cuadrática nos ayuda a resolver cualquier ecuación 
    cuadrática. Primero ponemos la ecuación en la forma ax²+bx+c=0, 
    donde a, b y c son coeficientes. Luego sustituimos estos coeficientes 
    en la fórmula: (-b±√(b²-4ac))/(2a) .

'''

def formulaCuadratica(a, b, c):
    raiz = cmath.sqrt( (b * b) - (4 * a * c) )
    x1 = (-b + raiz) / (2 * a)
    x2 = (-b - raiz) / (2 * a)
    return [x1, x2]

if __name__ == '__main__':
    
    print('Calculo de la formula cuadratica')
    
    print('Ingrese el valor de los terminos...')
    
    # a = int(input('a =  '))
    # b = int(input('b =  '))
    # c = int(input('c =  '))
    
    a = 5
    b = 2
    c = 1 
    
    x1, x2 = formulaCuadratica(a, b, c)
    
    print(f'x_1 = {x1}')
    print(f'x_2 = {x2}')