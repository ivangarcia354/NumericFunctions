import numpy as np
from math import sqrt

#FormaConvencional

a = float(input("Ingrese un valor para a\n"))
b = float(input("Ingrese un valor para b\n"))
c = float(input("Ingrese un valor para c\n"))

raiz_x1 = 0
raiz_x2 = 0

radicando = b**2 - 4*a*c

if radicando < 0:
    print ("La raiz no es real\n")
else:
    raiz_x1 = format((-b + sqrt(radicando)) / 2*a , ' .7g' )
    raiz_x2 = format((-b - sqrt(radicando)) / 2*a , ' .7g' )
    print("Las raices reales encontradas son \n x1 = {} \n x2 = {} \n " .format(raiz_x1, raiz_x2))
    
    