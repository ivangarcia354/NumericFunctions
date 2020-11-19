import matplotlib.pyplot as plt
import numpy as np


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

  # Pop the headers from the data array
  column_headers = data.pop(0)
  #row_headers = [x.pop(0) for x in data]
  # Table data needs to be non-numeric text. Format the data
  # while I'm at it.
  cell_text = []
  for row in data:
      cell_text.append([f'{x}' for x in row])
      #print(x)
  # Get some lists of color specs for row and column headers
  #rcolors = plt.cm.BuPu(np.full(len(row_headers), 0.1))
  ccolors = plt.cm.BuPu(np.full(len(column_headers), 0.1))
  # Create the figure. Setting a small pad on tight_layout
  # seems to better regulate white space. Sometimes experimenting
  # with an explicit figsize here can produce better outcome.
  plt.figure(linewidth = 2,
             edgecolor = fig_border,
             facecolor = fig_background_color,
             tight_layout = {'pad':1},
             figsize = (6, iteraciones*(4/6))
            )
  # Add a table at the bottom of the axes
  the_table = plt.table(cellText = cell_text,
                        #rowLabels = row_headers,
                        #rowColours = rcolors,
                        rowLoc = 'center',
                        colColours = ccolors,
                        colLoc = 'center',
                        colLabels = column_headers,
                        colWidths = [0.15,0.3,0.15,0.15,0.15],
                        loc = 'center')
  # Scaling is the only influence we have over top and bottom cell padding.
  # Make the rows taller (i.e., make cell y scale larger).
  the_table.scale(1, 2)
  # Hide axes
  ax = plt.gca()
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  # Hide axes border
  plt.box(on = None)
  # Add title
  plt.suptitle(title_text)
  # Add footer
  plt.figtext(0.95, 0.05, footer_text, horizontalalignment = 'right', size = 6, weight = 'heavy')
  # Force the figure to update, so backends center objects correctly within the figure.
  # Without plt.draw() here, the title will center on the axes and not the figure.
  plt.draw()
  # Create image. plt.savefig ignores figure edge and face colors, so map them.
  fig = plt.gcf()
  plt.savefig(file_name + '.png',
              #bbox='tight',
              edgecolor = fig.get_edgecolor(),
              facecolor = fig.get_facecolor(),
              dpi = 150
              )    
  return

def GeneraeConvTabla(data, iteraciones, title_text, file_name):
    
    x=[]
    y1=[]
    y2=[]
    i=0
    while i<4:
        data.pop(0)
        i+=1
    
    for i in data:
        x.append(i[0])
        y1.append(i[3])
        y2.append(i[4])
        
    fig, axs = plt.subplots(1, 2, figsize=(12, 4), sharey=True)
    
    axs[0].plot(x,y1)
    plt.ylabel('lambda',fontsize=10)
    plt.xlabel('Iteraciones',fontsize=15)
    plt.grid(True)
    
    
    axs[1].plot(x,y2)
    plt.ylabel('convergencia P',fontsize=10)
    plt.xlabel('Iteraciones',fontsize=15)
    plt.grid(True)
    
    
    fig.suptitle(title_text)
    
    plt.savefig(file_name + '.png',
              #bbox='tight',
              edgecolor = fig.get_edgecolor(),
              facecolor = fig.get_facecolor(),
              dpi = 150
              ) 
    

    return
""" 
    fig, axs = plt.subplots(1, 2, figsize=(9, 3), sharey=True)
    axs[0].plot(x,y1)
    axs[1].plot(x,y2)   
    fig.suptitle(title_text)
    plt.savefig(file_name + '.png',
              #bbox='tight',
              edgecolor = fig.get_edgecolor(),
              facecolor = fig.get_facecolor(),
              dpi = 150
              ) 
    
  """  