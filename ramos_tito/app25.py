import libreria
import os

#ejercicio 25 llamar funcion: capacidad_eletrica
carg=int(os.sys.argv[1])
voltj=int(os.sys.argv[2])
msg=""
e=libreria.capacidad_electrica(carg,voltj,msg)
print(e)
