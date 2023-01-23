#* Odenar de mayor a menor tres numeros
if __name__ == "__main__":
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = int(input("Ingrese el tercer numero: "))

    if a > b and a > c:
        print(f"{a}")
        if b > c:
            print(f"{b}")
            print(f"{c}")
        else:
            print(f"{c}")
            print(f"{b}")
    elif b > a and b > c:
        print(f"{b}")
        if a > c:
            print(f"{a}")
            print(f"{c}")
        else:
            print(f"{c}")
            print(f"{a}")
    else:
        print(f"c")
        if b > a:
            print(b)
            print(a)
        else:
            print(a)
            print(b)
