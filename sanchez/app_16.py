import libreria
import os

# 16 funcion cadencia de tiro de balas del AK-47

x=int(os.sys.argv[1])
y=float(os.sys.argv[2])
w=libreria.cadencia_tiro(x,y)
print("La cadencia de tiro de un arma es de: ", w)
