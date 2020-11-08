import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Fuerza bruta
intento = 0
candado = 0
intentos = []


while candado < 100000:
    contraseña = np.random.randint(9999)
    
    while intento != 10000:
        if intento == contraseña:
            intentos.append(intento)
            intento = 0
            break
        intento += 1  
    candado +=1

frec, bins = np.histogram(intentos, range=(0, 10000), bins=1000)
print(frec)  
#%%
#Graficos 
n, bins, patches = plt.hist(x=intentos, bins=1000, color='#0504aa',
                            alpha=0.7, rwidth=0.7)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Intentos')
plt.ylabel('Frecuencia')
plt.title('Histograma')
maxfreq = n.max()
# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)