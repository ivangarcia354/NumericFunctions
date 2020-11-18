import BusquedaRaices as br
import numpy as np
import matplotlib.pyplot as plt

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
x = np.arange(0., 2*Radio, 0.01)

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
"""
raices = []
raiz_funcion = []
datos_nr_mod = []
datos_pf = []
datos_b = []
datos_nr = []
raiz_titulo = []

raiz_titulo.append('Raiz')
raiz_titulo.append('Error')
raices.append(raiz_titulo)
"""

#%%
#busqueda de semilla
(matriz_semilla_1, iteraciones_1) = br.RaizBiseccion(funcion, lim_inf, lim_sup, ERROR_BISECCION)

semilla = (matriz_semilla_1[iteraciones_1-1])[1]
cota_semilla = (matriz_semilla_1[iteraciones_1-1])[2]

#%%

(matriz_biseccion, iteraciones_biseccion) = br.RaizBiseccion(funcion, lim_inf, lim_sup, min_error)
print("\nBisección:\n",matriz_biseccion)
semilla_1 = semilla
semilla_2 = semilla + cota_semilla

(matriz_secante, iteraciones_secante) = br.RaizSecante(funcion, min_error, semilla_1, semilla_2)
print("\nSecante:\n",matriz_secante)
#print("datos_secante {0} {1} {2}".format(matriz_secante[iteraciones_secante-1].pop(1) ,matriz_secante[iteraciones_secante-1].pop(2),matriz_secante[iteraciones_secante-1].pop(3)))



(matriz_PF, iteraciones_PF) = br.RaizPF(funcion, min_error, semilla, cota_semilla)
print("\nPF:\n",matriz_PF)

(matriz_NR, iteraciones_NR) = br.RaizNR(funcion, f_prima, min_error, semilla, cota_semilla)
print("\nNR:\n",matriz_NR)

(matriz_NRM, iteraciones_NRM) = br.RaizNRmodificado(funcion, f_prima, f_segunda, min_error, semilla, cota_semilla)
print("\nNRM:\n",matriz_NRM)

#print(" Metodo Secante \nEl valor de la raiz es: {0} +- {1} \n Metodo Punto Fijo \nEl valor de la raiz es: {2} +- {3} \n Metodo Biseccion \nEl valor de la raiz es: {4} +- {5} \n  Metodo Newton Raphson \nEl valor de la raiz es: {6} +- {7} \n Metodo NR Modificado\nEl valor de la raiz es: {8} +- {9} \n ".format(raiz_secante, error_secante, raiz_pf, error_pf, raiz_biseccion, error_biseccion, raiz_nr, error_nr, raiz_nr_mod, error_nr_mod))

"""
import matplotlib.pyplot as plt
title_text = 'Biseccion'
footer_text = 'Analiis Numerico'
fig_background_color = 'skyblue'
fig_border = 'lightblue'
data = raices

# Pop the headers from the data array
column_headers = data.pop(0)
row_headers = [x.pop(0) for x in data]
# Table data needs to be non-numeric text. Format the data
# while I'm at it.
cell_text = []
for row in data:
    cell_text.append([f'{x}' for x in row])
    #print(x)
# Get some lists of color specs for row and column headers
rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))
# Create the figure. Setting a small pad on tight_layout
# seems to better regulate white space. Sometimes experimenting
# with an explicit figsize here can produce better outcome.
plt.figure(linewidth = 2,
           edgecolor = fig_border,
           facecolor = fig_background_color,
           tight_layout = {'pad':1},
           figsize = (3,3)
          )
# Add a table at the bottom of the axes
the_table = plt.table(cellText = cell_text,
                      rowLabels = row_headers,
                      rowColours = rcolors,
                      rowLoc = 'center',
                      colColours = ccolors,
                      colLoc = 'center',
                      colLabels = column_headers,
                      loc = 'center')
# Scaling is the only influence we have over top and bottom cell padding.
# Make the rows taller (i.e., make cell y scale larger).
the_table.scale(1, 2)
# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# Hide axes border
plt.box(on = None)
# Add title
plt.suptitle(title_text)
# Add footer
plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='heavy')
# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()
# Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.savefig('pyplot-table-demo.png',
            #bbox='tight',
            edgecolor = fig.get_edgecolor(),
            facecolor = fig.get_facecolor(),
            dpi = 150
            )    





data = raices_vector

# Pop the headers from the data array
column_headers = data.pop(0)
row_headers = [x.pop(0) for x in data]
# Table data needs to be non-numeric text. Format the data
# while I'm at it.
cell_text = []
for row in data:
    cell_text.append([f'{x}' for x in row])
    #print(x)
# Get some lists of color specs for row and column headers
rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))
# Create the figure. Setting a small pad on tight_layout
# seems to better regulate white space. Sometimes experimenting
# with an explicit figsize here can produce better outcome.
plt.figure(linewidth = 2,
           edgecolor = fig_border,
           facecolor = fig_background_color,
           tight_layout = {'pad':1},
           figsize = (3,3)
          )
# Add a table at the bottom of the axes
the_table = plt.table(cellText = cell_text,
                      rowLabels = row_headers,
                      rowColours = rcolors,
                      rowLoc = 'center',
                      colColours = ccolors,
                      colLoc = 'center',
                      colLabels = column_headers,
                      loc = 'center')
# Scaling is the only influence we have over top and bottom cell padding.
# Make the rows taller (i.e., make cell y scale larger).
the_table.scale(1, 2)
# Hide axes
ax = plt.gca()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# Hide axes border
plt.box(on = None)
# Add title
plt.suptitle(title_text)
# Add footer
plt.figtext(0.95, 0.05, footer_text, horizontalalignment='right', size=6, weight='heavy')
# Force the figure to update, so backends center objects correctly within the figure.
# Without plt.draw() here, the title will center on the axes and not the figure.
plt.draw()
# Create image. plt.savefig ignores figure edge and face colors, so map them.
fig = plt.gcf()
plt.savefig('pyplot-table-demoa.png',
            #bbox='tight',
            edgecolor = fig.get_edgecolor(),
            facecolor = fig.get_facecolor(),
            dpi = 150
            )
"""