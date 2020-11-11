<<<<<<< HEAD
import numpy as np
import sys

padrones=103887,104181,103839,104606
Radio = 4.25


#suma de los ultimos digitos de los padrones de los estudiantes del grupo

aux=0
n=0
for i in padrones:
    aux+=(int(repr(i)[-1]))
    n +=1
s=aux
porcentaje = s / (n * 9.5)

def V(x) :return np.pi * x**2 (3* Radio - x) / 3

def f(x): return V(x) - ( V(2*Radio) * porcentaje )

def f_prima(x) : return (np.pi * 2 * x * (3* Radio - x) / 3) -(np.pi * x **2 / 3)


=======
import numpy as np
import sys

padrones=103887,104181,103839,104606
Radio = 4.25


#suma de los ultimos digitos de los padrones de los estudiantes del grupo

aux=0
n=0
for i in padrones:
    aux+=(int(repr(i)[-1]))
    n +=1
s=aux
porcentaje = s / (n * 9.5)

def V(x) :return np.pi * x**2 (3* Radio - x) / 3

def f(x): return V(x) - ( V(2*Radio) * porcentaje )

def f_prima(x) : return (np.pi * 2 * x * (3* Radio - x) / 3) -(np.pi * x **2 / 3)


>>>>>>> 96e67e3f795fc8f1e3c65cd4fe21839a6a5a9afb
