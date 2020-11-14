import BusquedaRaices as br
import numpy as np

def f(t): return  t**2 + t - 1      #np.e**t -t -1

def f_prima(t): return  2*t + 1     #np.e**t - 1

def f_segunda(t): return 2      #np.e**t
 
#(raiz,error) = br.RaizNrmodifcado(p, p_prima, p_segunda, br.lim_inf, br.lim_sup, br.min_error)
min_error = float(input("inserte el error "))
lim_sup = float(input("inserte un límite superior "))
lim_inf = float(input("inserte un límite inferior "))


(raizb, errorb) = br.RaizNR(f_prima, f_segunda, lim_inf, lim_sup, min_error)

print("Raiz RaizBiseccion", raizb)
# Analizar si hace falta print("errorb", errorb)

(raiz1,error1) = br.RaizNRmodificado(f, f_prima, f_segunda,lim_inf, raizb, min_error)

(raiz2,error2) = br.RaizNRmodificado(f, f_prima, f_segunda,raizb, lim_sup, min_error)