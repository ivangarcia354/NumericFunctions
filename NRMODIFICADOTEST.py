import numpy as np
import sys

MSG_ERROR_COTAS="Error de selección de cotas"
COTA_ERROR = 0.00001

#min_error = float(input("inserte el error "))
#lim_sup = float(input("inserte un límite superior "))
#lim_inf = float(input("inserte un límite inferior "))


def p(t):
        return np.e**t -t -1

def round_up(n, decimals):
    multiplier = 10 ** decimals
    return np.ceil(n * multiplier) / multiplier

def pn(a,b): return (b+a)/2


def RaizBiseccion(funcion, lim_inf, lim_sup, min_error):
  
    if funcion(lim_inf)*funcion(lim_sup) >= 0:  
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


def RaizNrmodifcado(lim_inf, lim_sup, min_error): 
    
    def p(t):
        return np.e**t -t -2

    funcion = p

    (semilla, cota) = RaizBiseccion(funcion, lim_inf, lim_sup, 0.02)
    
    lim_sup = semilla + cota
    lim_inf = semilla - cota
    p = semilla
    
    
    
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

    print (raiz)
    print (error)
        
    return raiz, error  


(valor1, valor2) = RaizNrmodifcado(-1, 2, 0.000002)