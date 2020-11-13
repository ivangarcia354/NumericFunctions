import BusquedaRaices as br
import numpy as np

def p(t): return np.e**t -t -1

def p_prima(t): return np.e**t - 1

def p_segunda(t): return np.e**t
 
#(raiz,error) = br.RaizNrmodifcado(p, p_prima, p_segunda, br.lim_inf, br.lim_sup, br.min_error)

(raiz,error)= br.RaizNrmodifcado(p,p_prima,p_segunda,-1, 2, 0.000002)