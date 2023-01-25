
def es_multiplo(num, mod):
    if num%mod == 0:
        return True

if __name__ == "__main__":
    print("Verificar si un numero es multiplo de otro")
    num = int(input("Ingrese el numero: "))
    mod = int(input("Ingrese el multiplo: "))
    if es_multiplo(num, mod):
        print(f"{num} si es un multiplo de {mod}")
    else:
        print(f"{num} no es un multiplo de {mod}")