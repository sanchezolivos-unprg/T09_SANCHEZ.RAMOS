import libreria
import os

#ejercicio 21 llamar funcion: area_trapecio

bm=int(os.sys.argv[1])
bmayor=int(os.sys.argv[2])
alt=int(os.sys.argv[3])
msg=""
q=libreria.area_trapecio(bm,bmayor,alt,msg)
print(q)
