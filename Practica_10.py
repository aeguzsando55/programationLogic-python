''' 
    Una tienda desea calcular el valor de venta de sus productos con base a 
    - costo de compra (cc)
    - tipo de producto (perecedero-p, no perecedero-n)
    - tipo de corservacion (fro, ambiente)
    - su periodo de conservación en días
    - su periodo de almacenamiento
    - su volumen (en litros)
    - medio de almacenamiento (nevera, congelador, estantera o guacal)
    
    Realize los siguentes calculos:
    1. Calcular su costo de alamacenamiento (ca) en funcion del costo de compra (cc), tipo de producto(tp), 
        tipo de conservacion (tc), periodo de conservación (pc), periodo de almacenamiento (pa) y volumen (vol), 
        De acuerdo al tipo de producto (perecedero y no perecedero):
        a. si el tipo de conservacion (tc) es en frio y periodo de conservacion (pc) es menor a 100 dias, 
        entonces el costo de almacenmento (ca) es del 5%  del costo de compra (cc). Caso contrario pc es mayor
        a 100 días, el ca es igual a 10% del cc. 
            para productos con tc = ambiente, si el pa es menor a 20 dias, el ca es del 30% del cc. Si el pa es 
            mayor a 20 días, el ca es del 10% del cc. 
        b. Para productos no perecederos, si el volumen es igual o mayor a 50lts, el ca es del 10% del cc, sino
            es del 20% del cc
            
    2. Calcular el porcentaje de deprecacion del producto:
        a. si el pa es menor a 30 dias el producto se deprecia 5%
        b. si es mayor a 30 se deprecia un 15%.
        
    3. Calcular el costo de exhibicion:
        a. si es perecedero almacenado en nevera su ce es igual al ca * 2
        b. si es perecedero almacenado en congelador el ce es igual al ca. 
        c. Si es no perecedero almacenado en estanteria, el ce es igual al 5% del ca.
        d. Si es no perecedero almacenado en guacal, el ce es igual al 7% del ca.
        
    4. Calcular el valor del producto y valor de venta
        a. el valor del producto esta dado por la sma del cc + ca + ce * pdp
        b. el valor de venta, s es perecedero se le es aumentado un 40%, si no es perecedro se le aumenta un 20%
        
    5. Imprimir los calculos, desglosados en el sguente orden:
        i.   costo del producto cc
        ii.  costo de almacenamento
        iii. costo de exhibicion
        iv.  porcentaje de depreciación
        v.   valor del producto
        v.   valor de venta
'''

def costo_almacenaje(cc, tp, tc, pc, pa, vol):
    if (tp == 'p'): # Perecederos
        if (tc == 'f'): # Frios
            if (pc < 100): 
                return cc * 0.05
            else:
                return cc * 0.1
        else: # Ambiente
            if (pa < 20):
                return cc * 0.03    
            elif (pa > 20):
                return cc * 0.1
            else:
                return cc * 0.05
            
    else: # No perecederos
        if (vol >= 50):
            return cc * 0.1
        else:   
            return cc * 0.2
        
def calc_deprecacion(cc, pa):
    if (pa < 30):
        return cc * 0.05
    else:
        return cc * 0.15
    
def calc_costo_exhibicion(tp, ma, ca):
    if (tp == 'f'):
        if (ma == 'n'):
            return ca * 2
        else:
            return ca
    else:
        if(ma == 'e'):
            return ca * 0.05
        else:
            return ca * 0.07
        
def calc_valor_venta(vp, tp):
    if (tp == 'p'):
        return vp * 1.40
    else:
        return vp * 1.20
    

if __name__ == "__main__":
    print("DATOS DE ENTRADA:")
    cc = int(input("Ingrese el costo de compra .......................................................: "))
    tp = input("Ingrese el tipo de producto: P - Perecedero, N -No precededero........................: ").lower()
    tc = input("Ingrese el tipo de conserva: (F)rio, (A)mbiente.......................................: ").lower()
    pc = int(input("Ingrese el periodo de conserva en días............................................: "))
    pa = int(input("Ingrese el periodo de almacenamento en días.......................................: "))
    vol = int(input("Ingrese el volumen................................................................: "))
    if (tp == 'p'):
        ma = input("Ingrese el medio de almacenaje: (N)evera, (C)ongelador.................: ").lower()
    else:
        ma = input("Ingrese el medio de almacenaje: (E)stanteria o (G)uacal................: ").lower()
    
    ca = costo_almacenaje(cc, tp, tc, pc, pa, vol)
    pdp = calc_deprecacion(ca, pa)
    ce = calc_costo_exhibicion(tp, ma, ca)
    vp = cc + ca + ce * pdp
    vv = calc_valor_venta(vp, tp)
    
    print(f"ca: {ca} - pdp: {pdp} - ce: {ce} - vp: {vp} - vv: {vv}")