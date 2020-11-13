import BusquedaRaices as br
import numpy as np

padrones=103887,104181,103839,104606
Radio = 4.25


#suma de los ultimos digitos de los padrones de los estudiantes del grupo

aux=0
n=0
for i in padrones:
    aux+=(int(repr(i)[-1]))
    n +=1
s=aux
porcentaje = s / (n * 9.5)

def V(x):  return np.pi * x** 2 *(3* Radio - x) / 3

def f1(x):  return V(x) - ( V(2*Radio) * porcentaje )

def f2(x):  return V(x) - V(2*Radio) 

def f_prima(x):  return x * np.pi * (2 * Radio - x)

def f_segunda(x): return 2 * np.pi * (Radio - x)

funcion= f1

#(uno, dos) = br.RaizSecante(funcion, br.lim_inf, br.lim_sup, br.min_error)

#(uno, dos) = br.RaizPF(funcion, br.lim_inf, br.lim_sup, br.min_error)

#(uno, dos) = br.RaizBiseccion(funcion, br.lim_inf, br.lim_sup, br.min_error)

(uno, dos) = br.RaizNR(funcion, f_prima, br.lim_inf, br.lim_sup, br.min_error)

#(uno, dos) = br.RaizNRmodificado(funcion, f_prima, f_segunda, br.lim_inf, br.lim_sup, br.min_error)

print("El valor de la raiz es:{0} +- {1}".format(uno, dos))