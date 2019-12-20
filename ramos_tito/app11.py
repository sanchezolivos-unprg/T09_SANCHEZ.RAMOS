import libreria
import os
#ejercicio11 llamar funcion: hallar velocidad
distancia=int(os.sys.argv[1])
tiempo=int(os.sys.argv[2])
msg=""
v=libreria.hallar_velocidad(distancia,tiempo,msg)
print(v)
