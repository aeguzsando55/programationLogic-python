"""_summary_
En una escuela se busca calcular el valor de la matricula de los alumnos con base en dos criterios:
- El número de asignaturas inscritas
- El estrato socio-economico del alumno
El costo de la inscripción varia si se toman muchas asignaturas, cuyo costo de cada una es fijo y el valor de 
casa asgnatra extra se incrementa un 15% a partir de más de 8 asignaturas. 
Deacuerdo al estrato del alumno se aplica una condonacion o subsidio especifico. 
"""

def calc_matricula(alumno, valor_asignatura):
    if alumno["num_asignaturas"] <= 8:
        costo_matricula = alumno["num_asignaturas"] * valor_asignatura
    else:
        costo_matricula = (alumno["num_asignaturas"] * valor_asignatura) + \
            (alumno["num_asignaturas"] - 8) * (1 + (valor_asignatura * 0.15))
    condonacion = subsidio(alumno["estrato"])
    return costo_matricula * condonacion
    
    
def subsidio(estrato):
    if estrato =='a':
        return (1 - 0.80) # aplica una condonacon del 80%
    else:
        return (1 - 0.20) # aplica una condonacion del 20%
    
        
if __name__ == "__main__":
    print("Calcular el valor de la matricula")
    valor_asignatura = 60
    nombre = input("Ingrese el nombre del alumno: ")
    num_asigaturas = int(input("Ingrese el numero de asiganturas a cursar: "))
    estrato = input("Ingrese su estrato socio-economico ('a' o 'b'): ")
    
    alumno = {"nombre": nombre,
            "num_asignaturas": num_asigaturas,
            "estrato": estrato}
    
    costo_matricula = calc_matricula(alumno, valor_asignatura)
    
    print(f"El alumno {alumno}, con estrato {estrato}, pagará por su matricula el total de ${costo_matricula}")