import BusquedaRaices as br
import numpy as np
import matplotlib.pyplot as plt
import GeneradorTablas as tb
padrones = 103887, 104181, 103839, 104606
Radio = 4.25
lim_inf = 4
lim_sup = 6
min_error = 1 * 10**(-13)
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

#%%
#GRAFICO DE FUNCIONES
x = np.arange(0., 2 * Radio, 0.01)

#configuración f1(x) y f2(x) gráfico
ax = plt.subplot(131)

y1 = f1(x)
y2 = f2(x)
ax.plot(x,y1,color='r',label='f1(x)')
ax.plot(x,y2,color='b',label='f2(x)')
plt.ylabel('f1 [m^3] , f2 [m^3]',fontsize=10)
plt.xlabel('Altura [m]',fontsize=15)
plt.grid(True)
plt.legend()

#configuración f_prima(x) gráfico
ax = plt.subplot(132)

y3 = f_prima(x)
ax.plot(x,y3,color='c',label='f \'(x)')
plt.ylabel('f \' [m^2]',fontsize=10)
plt.xlabel('Altura [m]',fontsize=15)
plt.grid(True)
plt.legend()

#configuración f_segunda(x) gráfico
ax = plt.subplot(133)

y4 = f_segunda(x)
ax.plot(x,y4,color='m',label='f \'\'(x)')
plt.ylabel('f \'\' [m]',fontsize=10)
plt.xlabel('Altura [m]',fontsize=15)
plt.legend()
plt.grid(True)

plt.tight_layout(pad=5,rect =(0,0,3,1.5))
plt.show()

#%%
#MÉTODOS DE BUQUEDA DE RAICES
funcion = f1

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
(matriz_semilla_1, iteraciones_1) = br.RaizBiseccion(funcion, lim_inf, lim_sup, ERROR_BISECCION)

semilla = (matriz_semilla_1[iteraciones_1 - 1])[1]
cota_semilla = (matriz_semilla_1[iteraciones_1 - 1])[2]

#%%
header = ["Iteración", "Resultado", "Error", "laNDEAda", "p"]

(matriz_biseccion, iteraciones_biseccion) = br.RaizBiseccion(funcion, lim_inf, lim_sup, min_error)
matriz_biseccion.insert(0, header)
tb.GenerarTabla(matriz_biseccion, iteraciones_biseccion, "Biseccion", "Biseccion_graph")
semilla_1 = semilla
semilla_2 = semilla + cota_semilla

(matriz_secante, iteraciones_secante) = br.RaizSecante(funcion, min_error, semilla_1, semilla_2)
matriz_secante.insert(0, header)
tb.GenerarTabla(matriz_secante, iteraciones_secante, "Secante", "Secante_graph")


(matriz_PF, iteraciones_PF) = br.RaizPF(funcion, min_error, semilla, cota_semilla)
matriz_PF.insert(0,header)
tb.GenerarTabla(matriz_PF, iteraciones_PF, "PuntoFijo", "PuntoFijo_graph")

(matriz_NR, iteraciones_NR) = br.RaizNR(funcion, f_prima, min_error, semilla, cota_semilla)
matriz_NR.insert(0, header)
tb.GenerarTabla(matriz_NR, iteraciones_NR, "NR", "NR_graph")

(matriz_NRM, iteraciones_NRM) = br.RaizNRmodificado(funcion, f_prima, f_segunda, min_error, semilla, cota_semilla)
matriz_NRM.insert(0,header)
tb.GenerarTabla(matriz_NRM, iteraciones_NRM, "NR Modificado", "NrMod_graph")

