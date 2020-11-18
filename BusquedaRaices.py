import numpy as np
import sys

# Este archivo contiene todos los métodos numéricos utilizados en el Trabajo Práctico 1

MSG_ERROR_COTAS = "Error de selección de cotas"


#%%
#funciones 

def round_up(n, decimals):
    multiplier = 10 ** decimals
    return np.ceil(n * multiplier) / multiplier

def bisección(a,b): return (b+a)/2

#%%
#BISECCIÓN
def RaizBiseccion(funcion, lim_inf, lim_sup, min_error):
  
    matriz = []

    if ((funcion(lim_inf) * funcion(lim_sup) >= 0) | (lim_inf > lim_sup)):  
        sys.exit(MSG_ERROR_COTAS)
      
    
   
    i = 0
    b = lim_sup
    a = lim_inf
    ep = min_error + 1
    while abs(ep) > min_error:

        p = bisección(a, b)
        ep = abs(b - p)
        i += 1

       
        #print(i, "°  ", "{0} +- {1}".format(p,ep))

        if (funcion(p) * funcion(b)) < 0:
            a = p
        elif (funcion(p) * funcion(a)) < 0:
            b = p
        else :
            ep = 2.2250738585072009e-308
            break

        num_dig_error = int(np.ceil(abs(np.log10(ep))))   
        raiz = np.round(p, num_dig_error) 
        error = round_up(abs(ep), num_dig_error)
    
        raiz_vector = []
        
        raiz_vector.append(i)
        raiz_vector.append(raiz)
        raiz_vector.append(error)
        matriz.append(raiz_vector)
            
    print("Se hicieron", i, "iteraciones con el método de bisección\n")
    
    return matriz, i

#%%
#SECANTE Debe recibir una funcion a analizar, un error, una semilla y una cota para la semilla dada.
 
def RaizSecante(funcion, min_error, semilla_1, semilla_2): 
    
    
    matriz = []

    p_n_2 = semilla_2 
    p_n_1 = semilla_1
    aux = p_n_1 - p_n_2
    
    i = 0
    
    while abs(aux) > min_error:
      p = p_n_1 - ( ( funcion(p_n_1) * (p_n_1 - p_n_2 ) ) / ( funcion(p_n_1) - funcion(p_n_2) ) )
      p_n_2 = p_n_1
      p_n_1 = p
      aux = p_n_1 - p_n_2
      i+=1
      
      num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
      raiz = np.round(p, num_dig_error) 
      error = round_up(abs(aux), num_dig_error)
  
      raiz_vector = []
      raiz_vector.append(i)
      raiz_vector.append(raiz)
      raiz_vector.append(error)
      matriz.append(raiz_vector)
    
    print("\nSe hicieron", i, "iteraciones con el método de la secante\n")
    
    return matriz, i

#%%
#PUNTO FIJO Debe recibir una funcion a analizar, un error, una semilla y una cota dada para la semilla.

def RaizPF(funcion, min_error, semilla, cota_semilla): 
    
    k = 0.02
    def g(x) : return ( x -k* funcion(x))
    
    matriz = []
    
    #(semilla, cota) = RaizBiseccion(funcion, lim_inf, lim_sup, 0.02)
    p = semilla
    aux = cota_semilla
    
    
    i = 0
    while abs(aux) > min_error:
        
      p_next = g(p)
      aux =(p_next - p)
      p = p_next
      i += 1
      
      num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
      raiz = np.round(p_next, num_dig_error) 
      error = round_up(abs(aux),num_dig_error)      
      
      raiz_vector = []
      raiz_vector.append(i)
      raiz_vector.append(raiz)
      raiz_vector.append(error)
      matriz.append(raiz_vector)
    
    print("\nSe hicieron", i, "iteraciones con el método de Punto Fijo\n")
    
    return matriz, i

#%%
#Newton-Rhapson Debe recibir una funcion a analizar, su derivada, un error, una semilla y una cota dada para la semilla.
def RaizNR(funcion, f_prima, min_error, semilla, cota_semilla): 
    
    
    matriz = []
    
        
    p = semilla 
    aux = cota_semilla
    
    i = 0
    
    while abs(aux) > min_error:
      p_next = p - (funcion(p) / f_prima(p))
      aux = p_next - p
      p= p_next
      i+=1
      
      num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
      raiz = np.round(p, num_dig_error) 
      error = round_up(abs(aux),num_dig_error)      
      
      raiz_vector = []
      raiz_vector.append(i)
      raiz_vector.append(raiz)
      raiz_vector.append(error)
      matriz.append(raiz_vector)
      
      
    print("\nSe hicieron", i, "iteraciones con el método de Newton Raphson\n")
    
    return matriz, i

#%%
#Newton-Raphson Modificado
 
def RaizNRmodificado(funcion, f_prima, f_segunda, min_error, semilla, cota_semilla):
    
    #(semilla, cota) = RaizBiseccion(funcion, lim_inf, lim_sup, 0.02)
    
    matriz = []
      
    p = semilla 
    aux = cota_semilla
   
    i = 0
    
    while abs(aux) > min_error:
      p_next = p - (funcion(p) * f_prima(p)) / (( f_prima(p)) ** 2 - funcion(p) * f_segunda(p))
      aux = p_next - p
      p = p_next
      i += 1
      
      num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
      raiz = np.round(p, num_dig_error) 
      error = round_up(abs(aux),num_dig_error)      
      
      raiz_vector = []
      raiz_vector.append(i)
      raiz_vector.append(raiz)
      raiz_vector.append(error)
      matriz.append(raiz_vector)
      
    
    print("\nSe hicieron", i, "iteraciones con el método de Newton Raphson modificado\n")
    
    
    return matriz, i