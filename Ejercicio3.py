import BusquedaRaices as br
import numpy as np
import matplotlib.pyplot as plt
import GeneradorTablas as tb
padrones = 103887, 104181, 103839, 104606

Radio = 4.25


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

def f2(x):  return V(x) - V(2*Radio) 

def f_prima(x):  return x * np.pi * (2 * Radio - x)

def f_segunda(x): return 2 * np.pi * (Radio - x)

tb.Graficarfunciones(f1,f2,f_prima,f_segunda,Radio)

#%%
#MÉTODOS DE BUQUEDA DE RAICES
funcion = f1
FUNCTION_TAG= "_f1"

matriz_semilla_1 = []
iteraciones_1 = 0
matriz_biseccion = []
iteraciones_biseccion = 0
matriz_secante = []
iteraciones_secante = 0
matriz_PF = []
iteraciones_PF = 0
matriz_NR = []
iteraciones_NR = 0


#%%
#busqueda de semilla
semilla = 0.9
cota_semilla = Radio

#para Bisección
lim_inf = 0
lim_sup = 2*Radio

"""
(matriz_semilla_1, iteraciones_1) = br.RaizBiseccion(funcion, lim_inf, lim_sup, ERROR_BISECCION)

semilla = (matriz_semilla_1[iteraciones_1 - 1])[1]
cota_semilla = (matriz_semilla_1[iteraciones_1 - 1])[2]
"""

#para secante
semilla_1 = semilla
semilla_2 = semilla + cota_semilla

#%%Generación de matrices de iteraciones de los métodos


(matriz_biseccion, iteraciones_biseccion) = br.RaizBiseccion(funcion, lim_inf, lim_sup, max_error)


(matriz_secante, iteraciones_secante) = br.RaizSecante(funcion, max_error, semilla_1, semilla_2)


(matriz_PF, iteraciones_PF) = br.RaizPF(funcion, max_error, semilla, cota_semilla)


(matriz_NR, iteraciones_NR) = br.RaizNR(funcion, f_prima, max_error, semilla, cota_semilla)


(matriz_NRM, iteraciones_NRM) = br.RaizNRmodificado(funcion, f_prima, f_segunda, max_error, semilla, cota_semilla)


#%%Generación de gráficos
print("Generándose los gráficos...espere porfavor\n")
header = ["Iteración", "Resultado", "Error", "Lambda", "p"]

matriz_biseccion.insert(0, header)

tb.GenerarTabla(matriz_biseccion, iteraciones_biseccion, "Bisección con Error "+ str(max_error), "Bisección_graph_"+ str(max_error) + FUNCTION_TAG)
matriz_biseccion.pop(0)
tb.GeneraeConvGrafico(matriz_biseccion, iteraciones_biseccion, "Bisección convergencia", "Bisección_graph_convergenia"+ str(max_error) + FUNCTION_TAG)

matriz_secante.insert(0, header)
tb.GenerarTabla(matriz_secante, iteraciones_secante, "Secante con Error " + str(max_error), "Secante_graph_"+ str(max_error) + FUNCTION_TAG)
tb.GeneraeConvGrafico(matriz_secante, iteraciones_secante, "Secante convergencia", "Secante_graph_convergenia"+ str(max_error) + FUNCTION_TAG)

matriz_PF.insert(0,header)
tb.GenerarTabla(matriz_PF, iteraciones_PF, "PuntoFijo con Error " + str(max_error), "PuntoFijo_graph_"+ str(max_error)  + FUNCTION_TAG)
tb.GeneraeConvGrafico(matriz_PF, iteraciones_PF, "PuntoFijo convergencia","PuntoFijo_graph_convergencia"+ str(max_error) + FUNCTION_TAG)

matriz_NR.insert(0, header)
tb.GenerarTabla(matriz_NR, iteraciones_NR, "NR con Error " + str(max_error), "NR_graph_"+ str(max_error)  + FUNCTION_TAG)
tb.GeneraeConvGrafico(matriz_NR, iteraciones_NR, "NR convergencia", "NR_graph_convergenia"+ str(max_error)  + FUNCTION_TAG)

matriz_NRM.insert(0,header)
tb.GenerarTabla(matriz_NRM, iteraciones_NRM, "NR Modificado con Error " + str(max_error), "NrMod_graph"+ str(max_error)  + FUNCTION_TAG)
tb.GeneraeConvGrafico(matriz_NRM, iteraciones_NRM, "NR Modificado convergencia", "NRMod_graph_convergenia"+ str(max_error)  + FUNCTION_TAG)

print("Se descargaron los archivos \".png\" en la carpeta actual")