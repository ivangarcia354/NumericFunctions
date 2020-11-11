import numpy as np
import sys

MSG_ERROR_COTAS="Error de selección de cotas"
COTA_ERROR = 0.00001

min_error = float(input("inserte el error "))
lim_sup = float(input("inserte un límite superior "))
lim_inf = float(input("inserte un límite inferior "))




def f1(x): return 0.25*x**2 - np.sin(x)
#cotas de f1: 2° raiz: max=3,min=1

def f2(x) : return np.exp(x/4) - x
#cotas de f2: 1° raiz: max=2,min=1
#             2° raiz: max=9,min=8

def f3(x) : return 1 - x - np.exp( -2*x )
#cotas de f3: 2° raiz: max=1,min=0.5

def f4(x) : return np.pi * (-1/3 *x**3 + 3*x**2 - 126/5)
#cotas de f4: max=5,min=1

def round_up(n, decimals):
    multiplier = 10 ** decimals
    return np.ceil(n * multiplier) / multiplier

def pn(a,b): return (b+a)/2

def RaizBiseccion(funcion, lim_inf, lim_sup, min_error):
  
    if funcion(lim_inf)*funcion(lim_sup) >=0:  
        print(MSG_ERROR_COTAS) 
        sys.exit(1)
      
    print("Iteraciones del método de Bisección\n")
    n=int(np.log2((lim_sup-lim_inf)/min_error))
    print("cantidad de iteraciones para hacer", n)

    i=0
    b=lim_sup
    a=lim_inf
    
    while i < (n):

        p = pn(a,b)
        ep = abs(b-p)
        i+=1
        print(i,"°  ","{0} +- {1}".format(p,ep))

        if (funcion(p)*funcion(b)) < 0:
            a = p
        elif (funcion(p)*funcion(a) < 0):
            b = p
        else :
            print("Hay algo que no esta bien")
            break
            
    print("Se hicieron",i,"iteraciones con el método de bisección\n")
    
    num_dig_error = int(np.ceil(abs(np.log10(min_error))))   
    ep=round_up(abs(ep),num_dig_error)
    
    return p,ep

"""
-------------------------------------------------------------------------------
--------------------------------------------------------------------------------
"""

def RaizSecante(funcion, lim_inf, lim_sup, min_error): 
    
    (semilla,cota) = RaizBiseccion(funcion,lim_inf,lim_sup,0.02)
    
    lim_sup = semilla + cota
    lim_inf = semilla - cota
    p = semilla
    
    print("Iteraciones del método de la secante\n")
    
    #las varibles lim_sup,lim_inf y p están para luego analizar bien las condiciones necesarias para el uso del Método de la secante
    p_n_2 = lim_sup 
    p_n_1 = p
    aux = p_n_1 - p_n_2
    
    i=1
    print(i,"°  ",p)
    
    while abs(aux) > min_error:
      p = p_n_1 - ( ( funcion(p_n_1) * (p_n_1 - p_n_2 ) ) / ( funcion(p_n_1) - funcion(p_n_2) ) )
      p_n_2 = p_n_1
      p_n_1 = p
      aux = p_n_1 - p_n_2
      print(i+1,"°  ",p)
      i+=1
    
    print("\nSe hicieron", i, "iteraciones con el método de la secante\n")
    
    num_dig_error = int(np.ceil(abs(np.log10(min_error))))   
    raiz = np.round(p, num_dig_error) 
    error = round_up(abs(aux),num_dig_error)
    
    return raiz,error

"""
-------------------------------------------------------------------------------
--------------------------------------------------------------------------------
"""

def g(x) : return (funcion(x) + x)

def RaizPF(funcion, lim_inf, lim_sup, min_error): 
    
    (semilla, cota) = RaizBiseccion(funcion, lim_inf, lim_sup, 0.02)
    lim_sup = semilla + cota
    lim_inf = semilla - cota
    p = semilla
    
    print("Iteraciones del método del Punto fijo\n")
    
    p_next = g(p)
    aux = p_next - p
    
    i=1
    print(i, "°  ", p_next)
    
    while abs(aux) > min_error:
    
      p_next = g(p)
      aux = (p_next - p)
      p = p_next
      i += 1
      print(i, "°  ", p_next)
    
    print("\nSe hicieron", i, "iteraciones con el método del Punto Fijo\n")
    
    num_dig_error = int(np.ceil(abs(np.log10(min_error))))   
    raiz = np.round(p_next, num_dig_error) 
    error = round_up(abs(aux),num_dig_error)
    return raiz, error


"""-------------------------------------------------------------------------------"""


funcion = f4

#(raiz,error)=RaizBinomial(funcion, lim_inf, lim_sup, min_error)

(raiz,error) = RaizSecante(funcion, lim_inf, lim_sup, min_error)

#(raiz,error)=RaizPF(funcion, lim_inf, lim_sup, min_error)

print("El valor de la raiz es:{0} +- {1}".format(raiz,error))
print("El valor de la función en la aproximación a la raiz es: ", funcion(raiz))

#%%
#Newton-Rhapson
    
def p(t):
    return (t - 3) * (t + 5)

def p_prima(t):
    return 2 * t + 2

iteracion = 0
semilla = -0.9
error = 1

while error > COTA_ERROR:
    iteracion += 1
    raiz = semilla - p(semilla) / p_prima(semilla)
    error = np.abs(raiz - semilla)
    semilla = raiz
    print(iteracion, raiz, error)
    

#%%
#Newton-Raphson Mod
def p(t):
    return np.e**t -t -1
def p_prima(t):
    return np.e**t - 1
def p_segunda(t):
    return np.e**t

iteracion = 0
semilla = 1
error = 1

while error > COTA_ERROR:
    iteracion += 1
    raiz = semilla - (p(semilla) * p_prima(semilla)) / ((p_prima(semilla))**2 - p(semilla) * p_segunda(semilla))
    error = np.abs(raiz - semilla)
    semilla = raiz
    print(iteracion, raiz, error)

def RaizNrmodifcado(funcion, lim_inf, lim_sup, min_error): 
    
    (semilla, cota) = RaizBiseccion(funcion, lim_inf, lim_sup, 0.02)
    
    lim_sup = semilla + cota
    lim_inf = semilla - cota
    p = semilla
    
    print("Iteraciones del método de la secante\n")
    
    #las varibles lim_sup,lim_inf y p están para luego analizar bien las condiciones necesarias para el uso del NR modificado
    p_n_2 = lim_sup 
    p_n_1 = p
    aux = p_n_1 - p_n_2
    
    i=1
    print(i, "°  ", p)
    
    def p(t):
        return np.e**t -t -1
    def p_prima(t):
        return np.e**t - 1
    def p_segunda(t):
        return np.e**t

iteracion = 0


while cota > COTA_ERROR:
    iteracion += 1
    raiz = semilla - (p(semilla) * p_prima(semilla)) / ((p_prima(semilla))**2 - p(semilla) * p_segunda(semilla))
    cota = np.abs(raiz - semilla)
    semilla = raiz
    

    
print("\nSe hicieron", iteracion, "iteraciones con el método de NR Mejorado\n")
    
num_dig_error = int(np.ceil(abs(np.log10(min_error))))   
raiz = np.round(p, num_dig_error) 
error = round_up(abs(aux), num_dig_error)
    
return raiz, error  