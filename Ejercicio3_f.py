import numpy as np
from scipy.optimize import brentq
import scipy as sci
import BusquedaRaices as br
import sys


padrones = 103887, 104181, 103839, 104606
Radio = 4.25
lim_inf = -1
lim_sup = 10
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

def f_prima(x):  return x * np.pi * (2 * Radio - x)

def f_segunda(x): return 2 * np.pi * (Radio - x)

print(sci.optimize.brentq(f1, lim_inf, lim_sup, full_output = True))

# Derivada

def f(t): return  a*t**2 + b*t + c      

def f_prima(t): return  2*a*t + b     

def f_segunda(t): return 2*a     
 
ERROR_BISECCION = 0.02
MSG_ERROR_RAIZ = "La raiz no es real\n"

min_error = 10**(-13)
lim_sup = 400
lim_inf = -10
a = -np.pi
b = np.pi*2*Radio
c = 0

radicando = b**2 - 4*a*c

if radicando < 0:
    sys.exit(MSG_ERROR_RAIZ)


#busqueda de pico de la función
(matriz_sem_pico, it_pico) = br.RaizBiseccion(f_prima, lim_inf, lim_sup, ERROR_BISECCION)

sem_pico = (matriz_sem_pico[it_pico - 1])[1]
cota_sem_pico = (matriz_sem_pico[it_pico - 1])[2]


(matriz_pico, it_pico) = br.RaizNR(f_prima, f_segunda, min_error, sem_pico, cota_sem_pico)

pico = (matriz_pico[it_pico - 1])[1]
error_pico = (matriz_pico[it_pico - 1])[2]

#primer raiz
(matriz_sem_1, it_sem_1) = br.RaizBiseccion(f, lim_inf, pico, ERROR_BISECCION)

sem_1 = (matriz_sem_1[it_sem_1 - 1])[1]
cota_sem_1 = (matriz_sem_1[it_sem_1 - 1])[2]

(matriz_raiz_1, it_raiz_1) = br.RaizNR(f, f_prima, min_error, sem_1, cota_sem_1)

#segunda raiz
(matriz_sem_2, it_sem_2) = br.RaizBiseccion(f, pico, lim_sup, ERROR_BISECCION)

sem_2 = (matriz_sem_2[it_sem_2 - 1])[1]
cota_sem_2 = (matriz_sem_2[it_sem_2 - 1])[2]

(matriz_raiz_2, it_raiz_2) = br.RaizNR(f, f_prima, min_error, sem_2, cota_sem_2)

raiz_1 = format((matriz_raiz_1[it_raiz_1 - 1])[1], '.7g')
raiz_2 = format((matriz_raiz_2[it_raiz_2 - 1])[1], '.7g')
error_raiz_1 = format((matriz_raiz_1[it_raiz_1 - 1])[2], '.7g')
error_raiz_2 = format((matriz_raiz_2[it_raiz_2 - 1])[2], '.7g')

print("Las raices reales encontradas para la derivada son \n x1 = {} +- {} \n x2 = {} +- {} \n " .format(raiz_1, error_raiz_1, raiz_2, error_raiz_2))
