import matplotlib.pyplot as plt
import numpy as np

def Graficarfunciones(f1,f2,f_prima,f_segunda,Radio):
    x = np.arange(0., 2 * Radio, 0.01)
    
    #configuración f1(x) y f2(x) gráfico
    ax = plt.subplot(131)
    
    y1 = f1(x)
    y2 = f2(x)
    ax.plot(x,y1,color='r',label='f1(x)')
    ax.plot(x,y2,color='b',label='f2(x)')
    plt.ylabel('f1 [m^3] , f2 [m^3]',fontsize=10)
    plt.xlabel('Altura [m]',fontsize=15)
    plt.grid(True)
    plt.legend()
    
    #configuración f_prima(x) gráfico
    ax = plt.subplot(132)
    
    y3 = f_prima(x)
    ax.plot(x,y3,color='c',label='f \'(x)')
    plt.ylabel('f \' [m^2]',fontsize=10)
    plt.xlabel('Altura [m]',fontsize=15)
    plt.grid(True)
    plt.legend()
    
    #configuración f_segunda(x) gráfico
    ax = plt.subplot(133)
    
    y4 = f_segunda(x)
    ax.plot(x,y4,color='m',label='f \'\'(x)')
    plt.ylabel('f \'\' [m]',fontsize=10)
    plt.xlabel('Altura [m]',fontsize=15)
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout(pad=5,rect =(0,0,3,1.5))
    plt.show()
    return

def GenerarTabla(data, iteraciones, title_text, file_name):


  if(iteraciones > 12):
    k = 0
    data_aux = []
    while k <= 6:
      data_aux.append(data[k])
      k += 1
    j = iteraciones - 5
    while j <= iteraciones:
      data_aux.append( data[j])
      j += 1

    data = data_aux
    iteraciones = 12
    
  footer_text = 'Analisis Numerico'
  fig_background_color = 'skyblue'
  fig_border = 'lightblue'

  column_headers = data.pop(0)
  cell_text = []
  
  for row in data:
      cell_text.append([f'{x}' for x in row])
      
  ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))
  
  plt.figure(linewidth = 2,
             edgecolor = fig_border,
             facecolor = fig_background_color,
             tight_layout = {'pad':1},
             figsize = (6, iteraciones*(4/6))
            )
  
  the_table = plt.table(cellText = cell_text,
                        rowLoc = 'center',
                        colColours = ccolors,
                        colLoc = 'center',
                        colLabels = column_headers,
                        colWidths = [0.15,0.3,0.15,0.15,0.15],
                        loc = 'center')
  
  the_table.scale(1, 2)
  ax = plt.gca()
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  plt.box(on = None)
  plt.suptitle(title_text)
  plt.figtext(0.95, 0.05, footer_text, horizontalalignment = 'right', size = 6, weight = 'heavy')
  plt.draw()
  fig = plt.gcf()
  plt.savefig('imagenes/'+file_name + '.png',
              edgecolor = fig.get_edgecolor(),
              facecolor = fig.get_facecolor(),
              dpi = 150
              )    
  return

def GeneraeConvGrafico(data, iteraciones, title_text, file_name):
    
    x=[]
    y1=[]
    y2=[]
    i=1
    
    if(iteraciones>3):
        while i<=3:
            data.pop(0)
            i+=1
    
    else: return
    
    for k in data:
        x.append(int(k[0]))
        y1.append(float(k[3]))
        y2.append(float(k[4]))
        
    fig, axs = plt.subplots(1, 2, figsize=(12, 4), sharey=False)
    
    axs[0].scatter(x,y1)
    axs[0].set_title('lambda',fontsize=10)
    axs[0].set_xlabel('Iteraciones',fontsize=15)
    axs[0].grid(True)
    
    axs[1].scatter(x,y2)
    axs[1].set_title('convergencia P',fontsize=10)
    axs[1].set_xlabel('Iteraciones',fontsize=15)
    axs[1].grid(True)
    
    
    fig.suptitle(title_text)
    
    plt.savefig('imagenes/'+file_name + '.png',
              edgecolor = fig.get_edgecolor(),
              facecolor = fig.get_facecolor(),
              dpi = 150
              ) 
    

    return
