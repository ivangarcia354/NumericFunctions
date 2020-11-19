import BusquedaRaices as br
import numpy as np

def f(t): return  a*t**2 + b*t + c      

def f_prima(t): return  2*a*t + b     

def f_segunda(t): return 2*a      
 
ERROR_BISECCION = 0.02
MSG_ERROR_RAIZ = "La raiz no es real\n"

min_error = 10**(-13)
lim_sup = 40
lim_inf = -10
a = -9.6e7
b = 5000
c = 364 

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

print("Las raices reales encontradas son \n x1 = {} +- {} \n x2 = {} +- {} \n " .format(raiz_1, error_raiz_1, raiz_2, error_raiz_2))
