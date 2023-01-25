def es_bisiesto(year):
    # * Un año es bisiesto si es:
    # *  - Divisible entre 4.
    # *  - No divisible entre 100.
    # *  - Divisible entre 400.
    # * (2000 y 2400 son bisiestos pues aún siendo divisibles entre 100 lo son también entre 400.
    # * Pero los años 1900, 2100, 2200 y 2300 no lo son porque solo son divisibles entre 100).
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    print("Evaluar si el año es bisesto")
    year = int(input("Ingrese el año: "))
    if es_bisiesto(year):
        print(f"el año {year} SI es bisiesto")
    else:
        print(f"el año {year} NO es bisiesto ")
