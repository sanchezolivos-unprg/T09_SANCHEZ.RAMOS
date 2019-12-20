import libreria
import os

# 6 funcion calculo del peso

m=float(os.sys.argv[1])
e=int(os.sys.argv[2])
h=float(os.sys.argv[3])
q=libreria.pes_correcto(m,e,h)
print("El peso coorecto es: ", q)
