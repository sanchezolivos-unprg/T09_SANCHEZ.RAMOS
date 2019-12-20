import libreria
import os

# 10 funcion haltura desde arriba hasta el suelo

v=float(os.sys.argv[1])
t=float(os.sys.argv[2])
r=libreria.haltura(v,t)
print("La haltura es: ", r)
