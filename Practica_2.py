
#* Verficar el mayor de tres numeros
if __name__ == "__main__":
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))
    
    if (a > b and a > c):
        print(f"{a} es el mayor")
    elif (b > a and b > c):
        print(f"{b} es el mayor")
    else:
        print(f"{c} es el mayor")