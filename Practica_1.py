import numpy as np
import math

#* Operaciones aritemeticas simples
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1 , num2):
    return num1/num2

def potencia(num, n):
    return num**n

def raiz_cuadrada(num):
    return math.sqrt(num)

if __name__ == "__main__":
    print("hello world")
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    mi_suma = suma(num1, num2)
    print(f"la suma de {num1} y {num2} es igual a {mi_suma}")
    mi_resta = resta(num1, num2)
    print(f"la resta de {num1} y {num2} es igual a {mi_resta}")
    mi_multiplicacion = multiplicacion(num1, num2)
    print(f"el producto de {num1} y {num2} es igual a {mi_suma}")
    mi_division = division(num1, num2)
    print(f"la division entre  {num1} y {num2} es igual a {mi_division}")
    mi_potencia = potencia(num1, num2)
    print(f"{num1} a la {num2} es igual a {mi_potencia}")
    mi_raiz = raiz_cuadrada(num1)
    print(f"la raiz cuadrada de {num2} es igual a {mi_raiz}")