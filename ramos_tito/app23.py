import libreria
import os

#ejercicio23 llamar funcion:hallar_aceleracion

masa=int(os.sys.argv[1])
fuerza=int(os.sys.argv[2])
msg=""
j=libreria.hallar_aceleracion(masa,fuerza,msg)
print(j)
