# funcion 1: calculo de vista

def cal_vista (medicion_lentes,cantidad_lentes):
    resultado=((cantidad_lentes*medicion_lentes)/2)
    return resultado

# funcion 2: calculo de la fuerza de la inercia

def fuerza (masa_kg,aceleracion):
    resultado=(masa_kg*aceleracion)
    return resultado

# funcion 3: calculo del area del triangulo

def area_triangulo (base,haltura):
    calculo=((base*haltura)/2)
    return calculo

# funcion 4: volumen del cilindro

def volumen_cilindro (haltura,radio):
    resultado=(3.14*(radio**2)*haltura)
    return resultado

# funcion 5: volumen del prisma cuadrangular

def volumen_prisma (lado_base,haltura):
    resultado=((lado_base**2)*haltura)
    return resultado

# funcion 6: calculo del peso correcto

def pes_correcto (haltura,masa,edad):
    resultado=((masa*edad)*2/(haltura))
    return resultado

# funcion 7: promedio notas de un estudiante

def promedio (n1,n2,n3):
    resultado=((n1+n2+n3)/3)
    return resultado

# funcion 8: calculo de la distancia

def distancia (velocidad,tiempo):
    resultado=(velocidad*tiempo)
    return resultado

# funcion 9: area del triangulo rectangulo

def area_tri_rectangulo (cateto1,cateto2):
    import math
    resultado=(math.sqrt(cateto1**2+cateto2**2))
    return resultado

# funcion 10: calculo de la haltura al caer un objeto desde arriba al suelo

def haltura (velocidad_inicial,tiempo):
    resultado=((velocidad_inicial* tiempo) + (9.8 / 2) * (tiempo ** 2))
    return resultado

# funcion 11: volumen de una esfera

def vol_esfera (radio):
    resultado=(4 * (3.14 / 3) * (radio ** 3))
    return resultado

