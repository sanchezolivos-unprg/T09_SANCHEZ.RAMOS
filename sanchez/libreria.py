# funcion 1: calculo de vista

def cal_vista (medicion_lentes,cantidad_lentes):
    resultado=((cantidad_lentes*medicion_lentes)/2)
    return resultado
# fin_def

# funcion 2: calculo de la fuerza de la inercia

def fuerza (masa_kg,aceleracion):
    resultado=(masa_kg*aceleracion)
    return resultado
# fin_def

# funcion 3: calculo del area del triangulo

def area_triangulo (base,haltura):
    calculo=((base*haltura)/2)
    return calculo
# fin_def

# funcion 4: volumen del cilindro

def volumen_cilindro (haltura,radio):
    resultado=(3.14*(radio**2)*haltura)
    return resultado
# fin_def

# funcion 5: volumen del prisma cuadrangular

def volumen_prisma (lado_base,haltura):
    resultado=((lado_base**2)*haltura)
    return resultado
# fin_def

# funcion 6: calculo del peso correcto

def pes_correcto (haltura,masa,edad):
    resultado=((masa*edad)*2/(haltura))
    return resultado
# fin_def

# funcion 7: promedio notas de un estudiante

def promedio (n1,n2,n3):
    resultado=((n1+n2+n3)/3)
    return resultado
# fin_def

# funcion 8: calculo de la distancia

def distancia (velocidad,tiempo):
    resultado=(velocidad*tiempo)
    return resultado
# fin_def

# funcion 9: area del triangulo rectangulo

def area_tri_rectangulo (cateto1,cateto2):
    import math
    resultado=(math.sqrt(cateto1**2+cateto2**2))
    return resultado
# fin_def

# funcion 10: calculo de la haltura al caer un objeto desde arriba al suelo

def haltura (velocidad_inicial,tiempo):
    resultado=((velocidad_inicial* tiempo) + (9.8 / 2) * (tiempo ** 2))
    return resultado
# fin_def

# funcion 11: volumen de una esfera

def vol_esfera (radio):
    resultado=(4 * (3.14 / 3) * (radio ** 3))
    return resultado
# fin_def

# funcion 12: negocio

def negocio (cantidad,precio):
    resultado=(cantidad*100*precio)
    return resultado
# fin_def

# funcion 13: rapidez de un corredor

def rapidez (distancia,tiempo):
    resultado=((distancia/tiempo)*2)
    return resultado
# fin_def

# funcion 14: cargas electricas

def fuerza_electrica (carga1,carga2,distancia):
    resultado=(9000000000*carga1*carga2/(distancia**2))
    return resultado
# fin_def

# funcion 15: volumen de un cono recto

def volumen_cono (radio,haltura):
    resultado=(3.14*(radio**2)*haltura/3)
    return resultado
# fin_def

# funcion 16: cadencia de tiro de un arma Ak-47

def cadencia_tiro (cantidad_balas,calibre_arma):
    resultado=((cantidad_balas*calibre_arma)/60)
    return resultado
# fin_def

# funcion 17: area del trapecio

def area_trapecio (base_menor,base_mayor,haltura):
    resultado=((base_menor+base_mayor)*haltura/2)
    return resultado
# fin_def

# funcion 18: operacion matematica de cuatro numeros

def operacion (n1,n2,n3,n4):
    res=((n1+n4)*(n3+n2))
    return res
# fin_def

# funcion 19: multiplicacion de 3 numeros

def multiplicar (n1,n2,n3):
    result=(n1*n2*n3)
    return result
# fin_def

# funcion 20: pedir dni

def pedir_entero(msg):
    entero_invalido=True
    while(entero_invalido):
        valor=input(msg)
        entero_invalido=(valor.isdigit()==False)
        return int(valor)

def pedir_dni (msg):
    dni_invalido=True
    while (dni_invalido):
        valor=pedir_entero(msg)
        dni_invalido=(len(str(valor))!=8)
        return valor
# fin_def




