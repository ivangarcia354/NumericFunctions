import BusquedaRaices as br
import numpy as np

def f(t): return  a*t**2 + b*t + c      #np.e**t -t -1

def f_prima(t): return  2*a*t + b     #np.e**t - 1

def f_segunda(t): return 2*a      #np.e**t
 
#(raiz,error) = br.RaizNrmodifcado(p, p_prima, p_segunda, br.lim_inf, br.lim_sup, br.min_error)
ERROR_BISECCION = 0.02

min_error = 10**(-13)
lim_sup = 40
lim_inf = -10
a = -9.6e7
b = 5000
c = 364 




(semilla, cota_semilla) = br.RaizBiseccion(f_prima, lim_inf, lim_sup, ERROR_BISECCION)

(raizb, errorb) = br.RaizNR(f_prima, f_segunda, min_error, semilla, cota_semilla)

(semilla_1, cota_semilla_1) = br.RaizBiseccion(f, lim_inf, raizb, ERROR_BISECCION)

(raiz_x1, error_x1) = br.RaizNR(f, f_prima, min_error, semilla_1, cota_semilla_1)

(semilla_2, cota_semilla_2) = br.RaizBiseccion(f, raizb, lim_sup, ERROR_BISECCION)

(raiz_x2, error_x2) = br.RaizNR(f, f_prima, min_error, semilla_2, cota_semilla_2)

print("Las raices reales encontradas son \n x1 = {} +- {} \n x2 = {} +- {} \n " .format(raiz_x1, error_x1, raiz_x2, error_x2))
