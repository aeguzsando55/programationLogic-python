# Una empresa de envios planea realizar promociones a las tarifas de sus servicios con con base 
# al peso, el valor, el dia de la semana del envio y el tipo de pago.
# La tarifa responde directamente al peso de la mercancia, de modo que se aplican las siguetes reglas:
# - Si el peso es menor a 100kg se cobra 2000
# - Si es mayor o igual a 100, pero menor a 150, se cobra 2500
# - Si es mayor o igual a 150, pero menor a 200, se cobra 3000
# - S es mayor a 200 se cobra 3500
# De acuerdo al valor de la mercancia, un descuento se aplica a la tarifa:
# - Si el valor de la mercancia oscila entre 3000 y 6000, aplica 10%
# - Si el valor de la mercancia oscila entre 6001 y 10000, aplica 20%
# - Si el valor de la mercancia es de más de 1000, aplica 20%

def calcular_tarifa(peso_mercancia):
    if peso_mercancia < 100:
        return 2000
    elif (100 < peso_mercancia <= 150):
        return 2500
    elif (150 < peso_mercancia <= 200):
        return 3000
    else:
        return 3500
    
def calcular_descuento(valor, tarifa):
    if (3000 < valor <= 6000):
        return tarifa * 0.2
    elif (6000 < valor <= 10000):
        return tarifa * 0.15
    elif (valor > 10000):
        return tarifa * 0.1
    else:
        return 0

def asignar_promocion(tipo_pago, dia_semana, tarifa):
    if (dia_semana.lower() == 'l' and tipo_pago.lower() == 'e'):
        return tarifa * 0.1
    elif (tipo_pago.lower() == 't'):
        return tarifa * 0.05
    else:
        return 0
    
def desglose(peso, valor, tarifa, dcto, promo):
    print(f"Tarifa de  mercancia con valor de ${valor} y un peso de {peso}kg")
    print(f"   ${tarifa}")
    print(f"-  ${dcto} (Descuento)")
    print(f"-  ${promo}(Dcto promocional)")
    print(f"   ${tarifa - dcto - promo} ")

if __name__ == "__main__":
    peso_mercancia = 350
    valor_mercancia = 10000
    tipo_pago = "e"
    dia_semana = "l"
    
    tarifa = calcular_tarifa(peso_mercancia)
    descuento = calcular_descuento(valor_mercancia, tarifa)
    promoo = asignar_promocion(tipo_pago, dia_semana, tarifa)
    
    desglose(peso_mercancia, valor_mercancia, tarifa, descuento, promoo)