import numpy as np
import sys

# Este archivo contiene todos los métodos numéricos utilizados en el Trabajo Práctico 1

MSG_ERROR_COTAS = "Error de selección de cotas"
ERROR_COMPU = 2.2250738585072009e-308

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

			 
				
				if (funcion(p) * funcion(b)) < 0:
						a = p
				elif (funcion(p) * funcion(a)) < 0:
						b = p
				else :
						ep = ERROR_COMPU
						break

				num_dig_error = int(np.ceil(abs(np.log10(ep))))   
				raiz = np.round(p, num_dig_error) 
				error = round_up(abs(ep), num_dig_error)

				
				if i > 3 :
					landa = 0.5 
					conv = 1 
				
				else:
					landa = ""
					conv = ""
					
				raiz_vector = []
				
				raiz_vector.append(i)
				raiz_vector.append(raiz)
				raiz_vector.append(error)
				raiz_vector.append(landa)
				raiz_vector.append(conv)
				matriz.append(raiz_vector)
						
		print("Se hicieron", i, "iteraciones con el método de bisección\n")
		
		return matriz, i

#%%
#SECANTE Debe recibir una funcion a analizar, un error, una semilla y una cota para la semilla dada.
 
def RaizSecante(funcion, min_error, semilla_1, semilla_2): 
		
		
		matriz = []

		p_prev = semilla_2 
		p = semilla_1
		aux = p - p_prev
		p_prev2 = 0

		
		i = 0
		
		while abs(aux) > min_error:
			p_next = p - ( ( funcion(p) * (p - p_prev ) ) / ( funcion(p) - funcion(p_prev) ) )
			aux = p_next  - p
			i+=1
			
			if(aux == 0):
				raiz = p_next
				error = ERROR_COMPU
			else:
				num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
				raiz = np.round(p_next, num_dig_error) 
				error = round_up(abs(aux),num_dig_error)

			
			
			if i > 3 :

				delta_1 = abs(p_prev - p_prev2)
				delta_2 = abs(p - p_prev)
				delta_3 = abs(p_next - p)
				conv = np.log(delta_2 / delta_3)/np.log(delta_1 / delta_2)
				landa = delta_3 / (delta_2**conv)
				conv = format(conv, '.4g')
				landa = format(landa, '.4g')
			else:
				landa = ""
				conv = ""
			p_prev2 = p_prev
			p_prev = p
			p = p_next

			raiz_vector = []
			raiz_vector.append(i)
			raiz_vector.append(raiz)
			raiz_vector.append(error)
			raiz_vector.append(landa)
			raiz_vector.append(conv)
			matriz.append(raiz_vector)
		
		print("\nSe hicieron", i, "iteraciones con el método de la secante\n")
		
		return matriz, i

#%%
#PUNTO FIJO Debe recibir una funcion a analizar, un error, una semilla y una cota dada para la semilla.

def RaizPF(funcion, min_error, semilla, cota_semilla): 
		
		k = 0.02
		def g(x) : return ( x -k* funcion(x))
		
		matriz = []
		
		p = semilla
		aux = cota_semilla
		p_prev2 = 0
		p_prev = 0
		
		i = 0
		while abs(aux) > min_error:
				
			p_next = g(p)
			aux =(p_next - p)
			
			i += 1
			
			if(aux == 0):
				raiz = p_next
				error = ERROR_COMPU
			else:
				num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
				raiz = np.round(p_next, num_dig_error) 
				error = round_up(abs(aux),num_dig_error)

			
			if i > 3 :

				delta_1 = abs(p_prev - p_prev2)
				delta_2 = abs(p - p_prev)
				delta_3 = abs(p_next - p)
				conv = np.log(delta_2 / delta_3)/np.log(delta_1 / delta_2)
				landa = delta_3 / (delta_2**conv)
				conv = format(conv, '.4g')
				landa = format(landa, '.4g')
			else:
				landa = ""
				conv = ""
			p_prev2 = p_prev
			p_prev = p
			p = p_next

			
			raiz_vector = []
			raiz_vector.append(i)
			raiz_vector.append(raiz)
			raiz_vector.append(error)
			raiz_vector.append(landa)
			raiz_vector.append(conv)
			matriz.append(raiz_vector)
		
		print("\nSe hicieron", i, "iteraciones con el método de Punto Fijo\n")
		
		return matriz, i

#%%
#Newton-Rhapson Debe recibir una funcion a analizar, su derivada, un error, una semilla y una cota dada para la semilla.
def RaizNR(funcion, f_prima, min_error, semilla, cota_semilla): 
		
		
		matriz = []
		
				
		p = semilla 
		aux = cota_semilla
		p_prev = 0
		p_prev2 = 0
		
		i = 0
		
		while abs(aux) > min_error:
			p_next = p - (funcion(p) / f_prima(p))
			aux = p_next - p
			
			i += 1
			
			
			if(aux == 0):
				raiz = p_next
				error = ERROR_COMPU
			else:
				num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
				raiz = np.round(p_next, num_dig_error) 
				error = round_up(abs(aux),num_dig_error)

			if i > 3 :

				delta_1 = abs(p_prev - p_prev2)
				delta_2 = abs(p - p_prev)
				delta_3 = abs(p_next - p)
				conv = np.log(delta_2 / delta_3)/np.log(delta_1 / delta_2)
				landa = delta_3 / (delta_2**conv)
				conv = format(conv, '.4g')
				landa = format(landa, '.4g')
			else:
				landa = ""
				conv = ""  

			p_prev2 = p_prev
			p_prev = p
			p = p_next    
			
			raiz_vector = []
			raiz_vector.append(i)
			raiz_vector.append(raiz)
			raiz_vector.append(error)
			raiz_vector.append(landa)
			raiz_vector.append(conv)
			matriz.append(raiz_vector)
			
			
		print("\nSe hicieron", i, "iteraciones con el método de Newton Raphson\n")
		
		return matriz, i

#%%
#Newton-Raphson Modificado
 
def RaizNRmodificado(funcion, f_prima, f_segunda, min_error, semilla, cota_semilla):
		
		
		matriz = []
			
		p = semilla 
		aux = cota_semilla
		p_prev = 0
		p_prev2 = 0
	 
		i = 0
		
		while abs(aux) > min_error:
			p_next = p - (funcion(p) * f_prima(p)) / (( f_prima(p)) ** 2 - funcion(p) * f_segunda(p))
			aux = p_next - p
			
			i += 1
			
			if(aux == 0):
				raiz = p_next
				error = ERROR_COMPU
			else:
				num_dig_error = int(np.ceil(abs(np.log10(abs(aux)))))   
				raiz = np.round(p_next, num_dig_error) 
				error = round_up(abs(aux),num_dig_error)
			
			if i > 3 :

				delta_1 = abs(p_prev - p_prev2)
				delta_2 = abs(p - p_prev)
				delta_3 = abs(p_next - p)
				conv = np.log(delta_2 / delta_3)/np.log(delta_1 / delta_2)
				landa = delta_3 / (delta_2**conv)
				conv = format(conv, '.4g')
				landa = format(landa, '.4g')
			else:
				landa = ""
				conv = ""  

			p_prev2 = p_prev
			p_prev = p
			p = p_next

			raiz_vector = []
			raiz_vector.append(i)
			raiz_vector.append(raiz)
			raiz_vector.append(error)
			raiz_vector.append(landa)
			raiz_vector.append(conv)
			matriz.append(raiz_vector)
			
		
		print("\nSe hicieron", i, "iteraciones con el método de Newton Raphson modificado\n")
		
		
		return matriz, i