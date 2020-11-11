import numpy as np
import sys

MSG_ERROR_COTAS="Error de selección de cotas"

min_error = float(input("inserte el error "))
cota_mayor = float(input("inserte una cota superior "))
cota_menor = float(input("inserte una cota inferior "))


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

def MagnitudError(min_error):
    #solo para error <= 1
    num_dig_error=0
    aux=np.trunc(min_error)
    while aux==0:
        num_dig_error+=1
        aux=np.trunc(min_error*10**num_dig_error)
    return num_dig_error

def pn(a,b): return (b+a)/2

def RaizBinomial(funcion,cota_menor,cota_mayor,min_error):
  
    if funcion(cota_menor)*funcion(cota_mayor) >=0:  
        print(MSG_ERROR_COTAS) 
        sys.exit(1)
      
    print("\nIteraciones del método de Bisección\n")
    n=np.log2((cota_mayor-cota_menor)/min_error)
     
    p=pn(cota_menor,cota_mayor )
    ep=cota_mayor-p
    
    i=1
    print(i,"°  ","{0} +- {1}".format(p,ep))
    b=cota_mayor
    a=cota_menor
   
    while i<(n):
        if (funcion(p)*funcion(b)) < 0:
            a=p
            p=pn(a,b)
            ep=ep/2
            print(i+1,"°  ","{0} +- {1}".format(p,ep))
            i+=1
        elif (funcion(p)*funcion(a) < 0):
            b=p
            p=pn(a,b)
            ep=ep/2
            print(i+1,"°  ","{0} +- {1}".format(p,ep))
            i+=1
             
    print("\nSe hicieron",i,"iteraciones con el método de bisección\n")
    
    num_dig_error=MagnitudError(min_error)   
    ep=round_up(ep,num_dig_error)
    
    return p,ep

"""
-------------------------------------------------------------------------------
--------------------------------------------------------------------------------
"""

def RaizSecante(funcion,cota_menor,cota_mayor,min_error): 
    
    (semilla,cota) = RaizBinomial(funcion,cota_menor,cota_mayor,0.02)
    
    cota_mayor = semilla + cota
    cota_menor = semilla - cota
    p = semilla
    
    print("Iteraciones del método de la secante\n")
    
    #las varibles cota_mayor,cota_menor y p están para luego analizar bien las condiciones necesarias para el uso del Método de la secante
    p_n_2 = cota_mayor 
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
    
    print("\nSe hicieron",i,"iteraciones con el método de la secante\n")
    
    num_dig_error=MagnitudError(min_error)   
    raiz=np.round(p, num_dig_error) 
    error=round_up(abs(aux),num_dig_error)
    
    return raiz,error

"""
-------------------------------------------------------------------------------
--------------------------------------------------------------------------------
"""

def g(x) : return (funcion(x) + x)

def RaizPF(funcion,cota_menor,cota_mayor,min_error): 
    
    (semilla,cota) = RaizBinomial(funcion,cota_menor,cota_mayor,0.02)
    cota_mayor = semilla + cota
    cota_menor = semilla - cota
    p = semilla
    
    print("Iteraciones del método del Punto fijo\n")
    
    p_next = g(p)
    aux = p_next - p
    
    i=1
    print(i,"°  ",p_next)
    
    while abs(aux) > min_error:
    
      p_next = g(p)
      aux = (p_next - p)
      p = p_next
      print(i+1,"°  ",p_next)
      i+=1
    
    print("\nSe hicieron",i,"iteraciones con el método del Punto Fijo\n")
    
    num_dig_error=MagnitudError(min_error)   
    raiz=np.round(p_next, num_dig_error) 
    error=round_up(abs(aux),num_dig_error)
    return raiz,error


"""-------------------------------------------------------------------------------"""


funcion = f4

#(raiz,error)=RaizBinomial(funcion, cota_menor, cota_mayor, min_error)

(raiz,error)=RaizSecante(funcion, cota_menor, cota_mayor, min_error)

#(raiz,error)=RaizPF(funcion, cota_menor, cota_mayor, min_error)

print("El valor de la raiz es:{0} +- {1}".format(raiz,error))
print("El valor de la función en la aproximación a la raiz es: ",funcion(raiz))




