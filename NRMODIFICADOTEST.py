import BusquedaRaices as br
import numpy as np

def f(t): return  a*t**2 + b*t + c      #np.e**t -t -1

def f_prima(t): return  2*a*t + b     #np.e**t - 1

def f_segunda(t): return 2*a      #np.e**t
 
#(raiz,error) = br.RaizNrmodifcado(p, p_prima, p_segunda, br.lim_inf, br.lim_sup, br.min_error)
min_error = float(input("inserte el error "))
lim_sup = float(input("inserte un límite superior "))
lim_inf = float(input("inserte un límite inferior "))
a = float(input("inserte el valor de a"))
b = float(input("inserte el valor de b"))
c = float(input("inserte el valor de c")) 

(raizb, errorb) = br.RaizNR(f_prima, f_segunda, lim_inf, lim_sup, min_error)

print("Raiz RaizBiseccion", raizb)

(raiz_x1, error_x1) = br.RaizNRmodificado(f, f_prima, f_segunda,lim_inf, raizb, min_error)

(raiz_x2, error_x2) = br.RaizNRmodificado(f, f_prima, f_segunda,raizb, lim_sup, min_error)

print("Las raices reales encontradas son \n x1 = {} +- {} \n x2 = {} +- {} \n " .format(raiz_x1, error_x1, raiz_x2, error_x2))
