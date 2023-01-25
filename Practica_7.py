
# * Descuentos: Un vendedor de sillas ofrece descuentos a sus clientes dependiendo cuantas compren
# * Si el se llevan 5 o menos el descuento es de solo 10%
# * Si el numero es mayor a 5 se aplica un descuento del 20%
# * Si se llevan mas de 10 el descuento es del 30%
# * Calcule el costo de una venta en funcion de las sillas vendidas


def calc_venta(num, precio):
    venta = num * precio
    if num < 5:
        descuento = venta * 0.10
    elif num >= 5:
        descuento = venta * 0.20
    else:
        descuento = venta * 0.30
    neto = venta - descuento
    
    print(f"Se realiza una venta de ${venta} menos un descuento de ${descuento}, se paga un total de ${neto}")


if __name__ == "__main__":
    print("Calcular venta de sillas: ")
    precio_unitario = 400
    num_sillas = int(input("Sillas vendidas: "))
    calc_venta(num_sillas, precio_unitario)
