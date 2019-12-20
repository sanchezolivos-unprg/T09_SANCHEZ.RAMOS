import libreria
import os

#ejercicio 17 llamar  funcion: hallar_masa
pes=int(os.sys.argv[1])
graved=int(os.sys.argv[2])
msg=""
h=libreria.hallar_masa(pes,graved,msg)
print(h)
