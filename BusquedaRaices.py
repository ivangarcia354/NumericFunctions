import numpy as np
import sys

MSG_ERROR_COTAS="Error de selección de cotas"

min_error = float(input("inserte el error "))
lim_sup = float(input("inserte un límite superior "))
lim_inf = float(input("inserte un límite inferior "))


#ecuaciones de las funciones a estudiar

def f1(x): return 0.25*x**2 - np.sin(x)
#cotas de f1: 2° raiz: max=3,min=1

def f2(x) : return np.exp(x/4) - x
#cotas de f2: 1° raiz: max=2,min=1
#             2° raiz: max=9,min=8

def f3(x) : return 1 - x - np.exp( -2*x )
#cotas de f3: 2° raiz: max=1,min=0.5

def f4(x) : return np.pi * (-1/3 *x**3 + 3*x**2 - 126/5)
#cotas de f4: max=5,min=1


#%%
#funciones 

def round_up(n, decimals):
    multiplier = 10 ** decimals
    return np.ceil(n * multiplier) / multiplier

def bisección(a,b): return (b+a)/2

#%%
#BISECCIÓN
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

        p = bisección(a,b)
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
    raiz = np.round(p, num_dig_error) 
    error=round_up(abs(ep),num_dig_error)
    
    return raiz,error

#%%
#SECANTE

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

#%%
#PUNTO FIJO



def RaizPF(funcion, lim_inf, lim_sup, min_error): 
    
    def g(x) : return (funcion(x) + x)
    
    (semilla, cota) = RaizBiseccion(funcion, lim_inf, lim_sup, 0.02)
    lim_sup = semilla + cota
    lim_inf = semilla - cota
    p = semilla
    aux=cota
    
    print("Iteraciones del método de Punto fijo\n")
    
    i=0
    while abs(aux) > min_error:
    
      p_next = g(p)
      aux = (p_next - p)
      p = p_next
      i += 1
      print(i, "°  ", p_next)
    
    print("\nSe hicieron", i, "iteraciones con el método de Punto Fijo\n")
    
    num_dig_error = int(np.ceil(abs(np.log10(min_error))))   
    raiz = np.round(p_next, num_dig_error) 
    error = round_up(abs(aux),num_dig_error)
    return raiz, error
#%%
#Newton-Rhapson
def RaizNR(funcion, prima, lim_inf, lim_sup, min_error): 
    
    (semilla,cota) = RaizBiseccion(funcion,lim_inf,lim_sup,0.02)
        
    p=semilla 
    aux = cota
    
    print("Iteraciones del método de Newton Raphson:\n")
    i=0
    
    while abs(aux) > min_error:
      p_next = p - (funcion(p)/prima(p))
      aux = p_next - p
      p= p_next
      i+=1
      print(i,"°  ",p)
      
    
    print("\nSe hicieron", i, "iteraciones con el método de Newton Raphson\n")
    
    num_dig_error = int(np.ceil(abs(np.log10(min_error))))   
    raiz = np.round(p, num_dig_error) 
    error = round_up(abs(aux),num_dig_error)
    
    return raiz,error


#%%
#Newton-Raphson Modificado
 
def RaizNRmodificado(funcion, f_prima, f_segunda, lim_inf, lim_sup, min_error):
    
    (semilla,cota) = RaizBiseccion(funcion,lim_inf,lim_sup,0.02)
        
    p=semilla 
    aux = cota
    
    print("Iteraciones del método de Newton Raphson modificado:\n")
    i=0
    
    while abs(aux) > min_error:
      p_next = p - (funcion(p) * f_prima(p)) / (( f_prima(p)) ** 2 - funcion(p) * f_segunda(p))
      aux = p_next - p
      p= p_next
      i+=1
      print(i,"°  ",p)
      
    
    print("\nSe hicieron", i, "iteraciones con el método de Newton Raphson modificado\n")
    
    num_dig_error = int(np.ceil(abs(np.log10(min_error))))   
    raiz = np.round(p, num_dig_error)
    error = round_up(abs(aux),num_dig_error)
    
    return raiz,error

#%%
#iMPRESIÓN
#funcion = f3

#(raiz,error) = RaizBinomial(funcion, lim_inf, lim_sup, min_error)

#(raiz,error) = RaizPF(funcion, lim_inf, lim_sup, min_error)

#(raiz,error) = RaizSecante(funcion, lim_inf, lim_sup, min_error)

#(raiz,error) = RaizNR(funcion, prima, lim_inf, lim_sup, min_error)

#(raiz,error) = RaizNRmodifcado(funcion,prima,segunda, lim_inf, lim_sup, min_error)

#print("El valor de la raiz es:{0} +- {1}".format(raiz,error))
#print("El valor de la función en la aproximación a la raiz es: ", funcion(raiz))