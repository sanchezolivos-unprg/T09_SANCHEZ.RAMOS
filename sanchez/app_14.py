import libreria
import os

# 14 funcion cargas electricas

x=float(os.sys.argv[1])
y=float(os.sys.argv[2])
z=float(os.sys.argv[3])
l=libreria.fuerza_electrica(x,y,z)
print("La carga electrica es: ", l)
