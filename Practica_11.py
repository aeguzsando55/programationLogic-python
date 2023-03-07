

def ruta_a(pasajeros, viajes):
    valor = viajes * 5000
    if (50 < pasajeros <= 100):
        return valor * 1.05
    elif (100 < pasajeros <= 150):
        return valor * 1.06
    elif (150 < pasajeros <= 200):
        return valor * 1.07
    elif (pasajeros > 200):
        return (valor *1.08) + ((pasajeros - 200) * 50)
    else:
        return valor
    
def ruta_b(pasajeros, viajes):
    valor = viajes * 6000
    if (50 < pasajeros <= 100):
        return valor * 1.06
    elif (100 < pasajeros <= 150):
        return valor * 1.07
    elif (150 < pasajeros <= 200):
        return valor * 1.08
    elif (pasajeros > 200):
        return (valor *1.09) + ((pasajeros - 200) * 50)
    else:
        return valor
    
def ruta_c(pasajeros, viajes):
    valor = viajes * 8000
    if (50 < pasajeros <= 100):
        return valor * 1.01
    elif (100 < pasajeros <= 150):
        return valor * 1.02
    elif (150 < pasajeros <= 200):
        return valor * 1.03
    elif (pasajeros > 200):
        return (valor *1.04) + ((pasajeros - 200) * 50)
    else:
        return valor

def ruta_d(pasajeros, viajes):
    valor = viajes * 10000
    if (50 < pasajeros <= 100):
        return valor * 1.125
    elif (100 < pasajeros <= 150):
        return valor * 1.15
    elif (150 < pasajeros <= 200):
        return valor * 1.175
    elif (pasajeros > 200):
        return (valor *1.2) + ((pasajeros - 200) * 50)
    else:
        return valor

def calc_ingresos_pasajero(viajes, ruta, pasajeros):
    rutas = {
            "a": ruta_a,        
            "b": ruta_b,
            "c": ruta_c,
            "d": ruta_d       
        }
    valor = rutas[ruta](pasajeros, viajes) 
    return valor

def calc_ingresos_paquete(ruta, paquetes10, paquetes1020, paquetes20):
    valor = 0
    if(ruta == 'a' or ruta == 'b'):
        if(paquetes10 <= 50):
            valor = valor + (100 * paquetes10)
        elif(50 < paquetes10 <= 100):
            valor = valor + (200 * paquetes10)
        else:
            valor = valor + (300 * paquetes10) 
            
        if(paquetes1020 <= 50):
            valor = valor + (150 * paquetes1020)
        elif(50 < paquetes1020 <= 100):
            valor = valor + (250 * paquetes1020)
        else:
            valor = valor + (350 * paquetes1020) 
            
        if(paquetes20 <= 50):
            valor = valor + (200 * paquetes20)
        elif(50 < paquetes20 <= 100):
            valor = valor + (300 * paquetes20)
        else:
            valor = valor + (400 * paquetes20) 
    else:
        if(paquetes10 <= 50):
            valor = valor + (160 * paquetes10)
        elif(50 < paquetes10 <= 100):
            valor = valor + (260 * paquetes10)
        else:
            valor = valor + (360 * paquetes10) 
            
        if(paquetes1020 <= 50):
            valor = valor + (240 * paquetes1020)
        elif(50 < paquetes1020 <= 100):
            valor = valor + (340 * paquetes1020)
        else:
            valor = valor + (440 * paquetes1020) 
            
        if(paquetes20 <= 50):
            valor = valor + (320 * paquetes20)
        elif(50 < paquetes20 <= 100):
            valor = valor + (420 * paquetes20)
        else:
            valor = valor + (520 * paquetes20)
            
    return valor

def calc_pago_ayudante(total_ingresos):
    if (total_ingresos <= 10000):
        return total_ingresos * 0.05
    elif (10000 < total_ingresos <= 20000):
        return total_ingresos * 0.08
    elif (20000 < total_ingresos <= 40000):
        return total_ingresos * 0.1
    else:
        return total_ingresos * 0.13

def calc_pago_seguro(total_ingresos):
    if (total_ingresos <= 10000):
        return total_ingresos * 0.03
    elif (10000 < total_ingresos <= 20000):
        return total_ingresos * 0.04
    elif (20000 < total_ingresos <= 40000):
        return total_ingresos * 0.05
    else:
        return total_ingresos * 0.06

def calc_consumo(ruta, viajes, pasajeros, paquetes10, paquetes1020, paquetes20):
    
    rutas = {"a": (viajes*150),
            "b": (viajes*167),
            "c": (viajes*184),
            "d": (viajes*203)
        }
    
    kilometros = rutas[ruta]
    consumo = kilometros / (39*17)
    peso = ((pasajeros*60) + 
            (paquetes10*10) + 
            (paquetes1020*15) + 
            (paquetes20 * 20))
    if(5000 < peso <= 10000):
        return consumo + (consumo * 0.1)
    elif (peso > 10000):
        return consumo + (consumo*0.25)
    else:
        return consumo * 0.75

if __name__ == "__main__":
    print("hello world")
    # Datos de entrada
    viajes = int(input("Número de viajes: "))
    ruta = input("Ruta (A, B, C, D): ").lower()
    pasajeros = int(input("Número de pasajeros: "))
    paquetes10 = int(input("Número de paquetes de menos de 10kg: "))
    paquetes1020 = int(input("Número de paquetes entre 10 y 20 kg: "))
    paquetes20 = int(input("Número de paquetes de más de 20kg: "))

    # Calculos
    ingresos_pasajero = calc_ingresos_pasajero(viajes, ruta, pasajeros)
    ingresos_paquete = calc_ingresos_paquete(ruta, paquetes10, paquetes1020, paquetes20)
    total_ingresos = ingresos_pasajero + ingresos_paquete
    pago_ayudante = calc_pago_ayudante(total_ingresos)
    pago_seguro = calc_pago_seguro(total_ingresos)
    consumo_combustble = calc_consumo(ruta, viajes, pasajeros, paquetes10, paquetes1020, paquetes20)
    deducciones = pago_ayudante + pago_seguro + consumo_combustble
    liquidacion = total_ingresos - deducciones 
    print(ingresos_pasajero)
    print(ingresos_paquete)
    print(total_ingresos)
    print(pago_ayudante)
    print(pago_seguro)
    print(consumo_combustble)
    print(deducciones)
    print(liquidacion)