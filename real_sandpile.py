
# =============================================================================
# Imagine dropping one grain of sand at a time in the same spot. Grains of sand
# spill over and a pile is created. We are replicating this phenomenon here.
# Grains of sand are spilled onto a certain cell, and spill over into the
# adjacent cells when a threshold height seperation between adjacent cells is
# reached. This continue for as many iterations as the user desires.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from myFuncs import spill_shift,grid_shift

plt.close('all')

init={'size':9}
init['midsize']=int((init['size']+1)/2)-1
init['spillsize']=5
init['steps']=1000
showplot_steps=(init['steps']-0)/100+1
showplot=np.linspace(0,init['steps'],showplot_steps)
init['showplot']=showplot.tolist()

a = np.zeros(shape=(init['size'],init['size']))
grid_max=0

avalanche_sizes=[];

plt.ioff # Use non-interactive mode. Keep the figure up after script ends.

while a[1,1]==0 or a[1,init['size']-2]==0 or a[init['size']-2,1]==0 or a[init['size']-2,init['size']-2]==0:
    a[init['midsize'],init['midsize']]+=1
#    Creating shifted matrices
    shift=spill_shift(init,a)
    
    while np.any(shift['down']>=init['spillsize']) or np.any(shift['up']>=init['spillsize']) or np.any(shift['left']>=init['spillsize']) or np.any(shift['right']>=init['spillsize']):
        a=grid_shift(init,shift,a)        
        shift=spill_shift(init,a)      
          
#       Set border. Sand falls off grid.
        if np.any(a[0]!=0) or np.any(a[init['size']-1]!=0) or np.any(a[:,0]!=0) or np.any(a[:,init['size']-1]!=0):            
            a[0]=0
            a[init['size']-1]=0
            a[:,0]=0
            a[:,init['size']-1]=0        
        
        if np.max(a)>grid_max:
            grid_max=np.max(a)
        plt.figure(2)
        plt.clf()
        plt.imshow(a);
#        plt.title('Step Number: {}'.format(i))
        plt.clim(0,grid_max)
        plt.colorbar()
        plt.show()
        plt.pause(0.001)

print('############## Corners reached ##############')
    
for i in range(init['steps']+1):
    a[init['midsize'],init['midsize']]+=1
    shift=spill_shift(init,a)
    
    while np.any(shift['down']>=init['spillsize']) or np.any(shift['up']>=init['spillsize']) or np.any(shift['left']>=init['spillsize']) or np.any(shift['right']>=init['spillsize']):
        a=grid_shift(init,shift,a)        
        shift=spill_shift(init,a)
        
#        Get avalanche sizes for histogram
#        avalanche_sizes.append(len(indices[0])) 
        
#    while init['spillsize']+1 in a:
#        indices = np.asarray(np.where(a==init['spillsize']+1))
##       Get avalanche sizes for histogram
#        avalanche_sizes.append(len(indices[0])) 
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