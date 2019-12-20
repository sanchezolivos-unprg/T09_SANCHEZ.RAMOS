#ejercicio 1, funcion: area_circulo

def area_circulo(radio,pi):
    resultado=(radio*pi**2)
    return resultado
#fin_def

#ejercicio 2, funcion: area_triangulo -> si el area es mayor que 100 mostrar "area pequeña"

def area_triangulo(base,altura,msg):
    resultado=(base*altura)/2
    if (resultado>100):
        msg="el area es grande"
    #fin_if
    return resultado,msg
#fin_def

#ejercicio 3, funcion:  area_cuadrado
def area_cuadrado(lado):
    resultado=(lado**2)
    return resultado
#fin_def

#ejercicio 4, funcion: promedio_alumno-> si el promedio es menor que 10, mostrar "esta desaprobado"
def promedio_alumno(nota1,nota2,nota3,nota4,msg):
    resultado=(nota1+nota2+nota3+nota4)/4
    if (resultado<10):
        msg="el alumno ha desparobado"
    #fin_if
    return resultado,msg
#fin_def

#ejercicio 5, funcion: mayor_numero ->mostrar que un numero sea mayor que otro
def mayor(a,b):
    if(a>b):
        return a
    #fin_if
    else:
        return b
#fin_def

#jercicio6, funcion:numero_celular ->mostrar numeros de celulares validos
def numero_celular(msg):
    numero_invalido=True
    while(numero_invalido):
        nro_celular=int(msg)
        numero_invalido=(len(str(nro_celular))!=9)
    return int(nro_celular)
#fin_def

#ejercicio7, funcion:palindromo ->mostrar que son palindromos
def palindromo(cadena,msg):
    invertida = cadena[::-1]
    if (invertida == cadena):
        msg=(cadena+" es un palindromo")
    return msg
#fin_def

#ejercicio8, funcion:ingresar_contraseña ->mostrar contraseñas correctas de 5 digitos
def contraseña(msg):
    contraseña_invalidad=True
    while(contraseña_invalidad):
        contrase_corr=int(msg)
        contraseña_invalidad=(len(str(contrase_corr))!=5)
    return int(contrase_corr)
#fin_def

#ejercicio9, funcion:sumar_numeros ->si la suma es mayor que cero entonces es un numero positivo
def suma_numeros(n1,n2,n3,msg):
    resultado=(n1+n2+n3)
    if (resultado>0):
        msg="el resultado es positivo"
    return resultado,msg
#fin_def

#ejercicio10, funcion:ingresar _nombre ->sera un nombre correcto cuando tenga 5 caracteres

def pedir_nombre(msg):
    nombre_invalido=True
    while(nombre_invalido):
        nombre=msg
        nombre_invalido=(nombre.isdigit==True and len(nombre)!=5)
    return nombre

#ejercicio11, funcion:hallar_velocidad ->mostrar si la velocidad es mayor que 100 es un infractor

def hallar_velocidad(distancia,tiempo,msg):
    velocidad=(distancia/tiempo)
    if (velocidad>100):
        msg="usted es un infractor"
    return velocidad,msg


#ejercicio12, funcion: voltaje  ->mostrar si el volatje es mayor o igual que 200v  es alto voltaje

def voltaje(intensidad_corriente,resistencia_e,msg):
    vol=(intensidad_corriente*resistencia_e)
    if (vol>=200):
        msg="es alto voltaje"
    return vol,msg


#ejercicio13, funcion: volumen_celindro
def volumen_celindro(area_base,altura):
     resultado=(area_base*altura)
     return resultado


#ejercicio14, funcion: menor_numero ->mostrar que el numero es menor

def menor_numero(y,z):
    if(y>z):
        msg1=(y + " es mayor que" + z)
    #fin_if

    return msg1

#fin_def

#ejercicio 15, funcion: temperatura -> motrar temperaturas invalidas mayores que 37°c

def temperatura(msg):
    temperatura_inva=True
    while(temperatura_inva):
        valor=int(msg)
        temperatura_inva=(valor>=37)
    return valor
#fin_def

#ejercicio 16, funcion: peso
def peso(masa,gravedad):
    res=(masa*gravedad)
    return res
#fin_def

#ejercicio 17, funcion:hallar_masa ->si masa es mayor que 60 mostrar usted es obeso

def hallar_masa(peso,gravedad,msg):
    res=(peso/gravedad)
    if (res>=60):
        msg=" usted es obeso"
    return res,msg
#fin_def

#ejercicio 18, funcion : hallar_presion

def hallar_presion(fuerza,area):
    resu=(fuerza/area)
    return resu
#fin_def

#ejercicio 19, funcion : ingresar_ruc -> mostrar ruc validos

def numero_ruc(msg):
    numero_invalido=True
    while(numero_invalido):
        ruc=int(msg)
        numero_invalido=(len(str(ruc))!=11)
    return int(ruc)
#fin_def

#ejercicio 20, funcion :hallar_trapecio

def area_trapecio(base_mayor,base_menor,altura):
    resultado=(base_mayor*base_menor)*altura/2
    return resultado
#fin_def

#ejercicio 21, funcion :hallar_trapecio -> si el area del trapecio es mayor que 10000 mostrar el area es grande

def area_trapecio(base_mayor,base_menor,altura,msg):
    resultado=(base_mayor*base_menor)*altura/2
    if(resultado>=10000):
         msg="el area es grande"
    return resultado,msg
#fin_def

#ejercicio 22, funcion: hallar_aceleracion
def hallar_aceleracion(fuerza,masa):
    result=(fuerza*masa)
    return result
#fin_def

#ejercicio 23, funcion: hallar_aceleracion -> si la aceleracion es mayor que 300 mostrar aceleracion maxima

def hallar_aceleracion(masa,fuerza,msg):
    resultado=(masa*fuerza)
    if(resultado>=300):
         msg="aceleracion maxima"
    return resultado,msg
#fin_def

#ejercicio 24 funcion: capacidad_electrica

def capacidad_electrica(carga,voltaje):
    reslt=(carga*voltaje)
    return reslt
#fin_ef

#ejercicio 25 funcion: capacidad_electrica-> si la capacidad es mayor que 200 mostrar capacidad especial
def capacidad_electrica(carga,voltaje,msg):
    reslt=(carga*voltaje)
    if(reslt>=200):
         msg="capacidad especial"

    return reslt,msg
#fin_def