
import numpy as np
import matplotlib.pyplot as plt

init = {'size':17}
init['midsize']=int((init['size']+1)/2)-1
init['spillsize']=3
init['steps']=500
showplot_steps=(init['steps']-0)/50+1
showplot=np.linspace(0,init['steps'],showplot_steps)
init['showplot']=showplot.tolist()
del showplot,showplot_steps

a = np.zeros(shape=(init['size'],init['size']))

plt.ioff() # Use non-interactive mode. Keep the figure up after script ends.

for i in range(init['steps']):
    plt.clf()
    a[init['midsize'],init['midsize']]+=4
    while init['spillsize']+1 in a:
        plt.clf()
        indices = np.asarray(np.where(a==init['spillsize']+1))
#        print(indices)
        a[a>init['spillsize']]=0
#        Finding indices of spill-over elements, up, down, right, left
        row_centre=indices[0]
        row_down=[x+1 for x in indices[0]]
        row_up=[x-1 for x in indices[0]]
        col_centre=indices[1]
        col_right=[y+1 for y in indices[1]]
        col_left=[y-1 for y in indices[1]]
#        Add one to cell up
        a[(row_up,col_centre)] = a[(row_up,col_centre)]+1
#        Add one to cell down
        a[(row_down,col_centre)] = a[(row_down,col_centre)]+1
#        Add one to cell left
        a[(row_centre,col_left)] = a[(row_centre,col_left)]+1
#        Add one to cell right
        a[(row_centre,col_right)] = a[(row_centre,col_right)]+1
#        Set border. Sand falls off grid.
        if np.any(a[0]!=0) or np.any(a[init['size']-1]!=0) or np.any(a[:,0]!=0) or np.any(a[:,init['size']-1]!=0):
            a[0]=0
            a[init['size']-1]=0
            a[:,0]=0
            a[:,init['size']-1]=0
#   Try to display a new figure every # of iterations
    if i in init['showplot']:
        plt.imshow(a);
        plt.clim(0,4)
        plt.colorbar()
        plt.show()
        plt.pause(0.001)
