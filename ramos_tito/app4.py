import libreria
import os
#ejercicio4 llamar funcion : promedio_alumno
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
nota3=int(os.sys.argv[3])
nota4=int(os.sys.argv[4])
msg=""
p=libreria.promedio_alumno(nota1,nota2,nota3,nota4,msg)
print(p)
