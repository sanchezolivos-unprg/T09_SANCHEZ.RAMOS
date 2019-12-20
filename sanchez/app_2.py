import libreria
import os

# 2 funcion del calculo de la fuerza de inercia

m=float(os.sys.argv[1])
ac=float(os.sys.argv[2])
y=libreria.fuerza(m,ac)
print("La fuerza es: " + str(y) + " " + "Kg")
