import sys
import re
contraseña= sys.argv[1]
validar=re.search("^[A-Z][0-9]{3}[a-z]+[\W]{3}$", contraseña)

if validar!=None:
   print("la contraseña  es valida")
else:
    print("la contraseña no es valida")

#probando que se subió el que era