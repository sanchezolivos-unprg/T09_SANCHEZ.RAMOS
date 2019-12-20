import libreria
import os


#ejercicio 24 llamar funcion: capacidad_eletrica
carg=int(os.sys.argv[1])
voltj=int(os.sys.argv[2])
e=libreria.capacidad_electrica(carg,voltj)
print(e)
