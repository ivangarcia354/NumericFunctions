import BusquedaRaices as br
import numpy as np

def p(t): return  t**2 + t - 1      #np.e**t -t -1

def p_prima(t): return  2*t + 1     #np.e**t - 1

def p_segunda(t): return 2      #np.e**t
 
#(raiz,error) = br.RaizNrmodifcado(p, p_prima, p_segunda, br.lim_inf, br.lim_sup, br.min_error)
min_error = float(input("inserte el error "))
lim_sup = float(input("inserte un límite superior "))
lim_inf = float(input("inserte un límite inferior "))



(raiz,error)= br.RaizNRmodificado(p, p_prima, p_segunda,lim_inf, lim_sup, 0.000002)