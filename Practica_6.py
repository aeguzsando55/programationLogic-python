def calcular_salario(horas, valor_hora, salario_minimo):
    if horas > 8:
        horas_extra = horas - 8
        salario_neto = salario_minimo + (horas * valor_hora) + ((horas_extra * valor_hora)*1.20) 
    elif 6 < horas <= 8:
        salario_neto = salario_minimo + (horas * valor_hora)
    else:
        salario_neto = salario_minimo 
    
    return salario_neto
    
    

if __name__ == "__main__":
    print("Calcular salaro deacuerdo a horas trabajadas")
    horas = int(input("Horas trabajadas: "))
    valor_hora = int(input("valor de hora trabajada: "))
    salario_min = float(input("Salario mínimo: "))
    salario_calculado = calcular_salario(horas, valor_hora, salario_min)
    print(f"Recibirá la cantidad de ${salario_calculado}")
    