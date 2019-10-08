# =============================================================================
# Imagine dropping one grain of sand at a time in the same spot. Grains of sand
# spill over and a pile is created. We are replicating this phenomenon here.
# Grains of sand are spilled onto a certain cell, and spill over into the
# adjacent cells when a threshold height is reached. This continue for as many
# iterations as the user desires.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from myFuncs import spill

plt.close('all')

init = {'size':21}
init['midsize']=int((init['size']+1)/2)-1
init['spillsize']=3
init['steps']=100000
showplot_steps=(init['steps']-0)/10000+1
showplot=np.linspace(0,init['steps'],showplot_steps)
init['showplot']=showplot.tolist()
del showplot,showplot_steps

a = np.zeros(shape=(init['size'],init['size']))

avalanche_sizes=[];

plt.ioff # Use non-interactive mode. Keep the figure up after script ends.

while a[1,1]==0 or a[1,init['size']-2]==0 or a[init['size']-2,1]==0 or a[init['size']-2,init['size']-2]==0:
    a[init['midsize'],init['midsize']]+=4
    while init['spillsize']+1 in a:
        indices = np.asarray(np.where(a==init['spillsize']+1))
        a=spill(init,a,indices)
        
#       Set border. Sand falls off grid.
        if np.any(a[0]!=0) or np.any(a[init['size']-1]!=0) or np.any(a[:,0]!=0) or np.any(a[:,init['size']-1]!=0):            
            a[0]=0
            a[init['size']-1]=0
            a[:,0]=0
            a[:,init['size']-1]=0

print('############## Corners reached ##############')
    
for i in range(init['steps']+1):
    
    a[init['midsize'],init['midsize']]+=4
    while init['spillsize']+1 in a:
        indices = np.asarray(np.where(a==init['spillsize']+1))
#       Get avalanche sizes for histogram
        avalanche_sizes.append(len(indices[0])) 
        a=spill(init,a,indices)
#       Set border. Sand falls off grid.
        if np.any(a[0]!=0) or np.any(a[init['size']-1]!=0) or np.any(a[:,0]!=0) or np.any(a[:,init['size']-1]!=0):            
            a[0]=0
            a[init['size']-1]=0
            a[:,0]=0
            a[:,init['size']-1]=0
           
#   Try to display a new figure every # of iterations
    if i in init['showplot']:
        
        plt.figure(1)
        plt.clf()
#        hist, bins, _ = plt.hist(avalanche_sizes, bins=10)
#        bins=np.arange(np.max(avalanche_sizes))
#        plt.xticks()
        logbins=np.geomspace(min(avalanche_sizes), max(avalanche_sizes), 20)
        plt.hist(np.log(avalanche_sizes), log=True, bins=logbins)
        plt.xscale('log')
        plt.title('Step Number: {}'.format(i))
        plt.xlabel('Avalanche Size')
        plt.ylabel('Frequency')
        plt.show()
        plt.pause(0.001)
        
        plt.figure(2)
        plt.clf()
        plt.imshow(a);
        plt.title('Step Number: {}'.format(i))
        plt.clim(0,4)
        plt.colorbar()
        plt.show()
        plt.pause(0.001)
