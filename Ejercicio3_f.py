import numpy as np
from scipy.optimize import brentq
import scipy as sci


padrones = 103887, 104181, 103839, 104606
Radio = 4.25
lim_inf = 4
lim_sup = 6
max_error = 1 * 10**(-13)
ERROR_BISECCION = 0.02


#suma de los ultimos digitos de los padrones de los estudiantes del grupo
aux = 0
n = 0
for i in padrones:
    aux += (int(repr(i)[-1]))
    n +=1
s=aux
porcentaje = s / (n * 9.5)

def V(x):  return np.pi * x** 2 *(3* Radio - x) / 3

def f1(x):  return V(x) - ( V(2*Radio) * porcentaje )



print(sci.optimize.brentq(f1, lim_inf, lim_sup, full_output = True))

