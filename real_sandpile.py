
# =============================================================================
# Imagine dropping one grain of sand at a time in the same spot. Grains of sand
# spill over and a pile is created. We are replicating this phenomenon here.
# Grains of sand are spilled onto a certain cell, and spill over into the
# adjacent cells when a threshold height seperation between adjacent cells is
# reached. This continue for as many iterations as the user desires.
# =============================================================================
import numpy as np
import matplotlib.pyplot as plt
from myFuncs import spill_shift

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
#    D=np.insert(a,[-1],np.zeros((1,init['size'])),axis=0)
#    D=np.delete(D,0,axis=0)
#    U=np.insert(a,[0],np.zeros((1,init['size'])),axis=0)
#    U=np.delete(U,-1,axis=0)
#    L=np.insert(a,0,0,axis=1)
#    L=np.delete(L,-1,1)
#    R=(np.insert(a,-1,0,axis=1))
#    R=np.delete(R,0,1)
#    spill_down_shift=a-D
#    spill_up_shift=a-U
#    spill_left_shift=a-L
#    spill_right_shift=a-R
    
    while np.any(spill_down_shift>=init['spillsize']) or np.any(spill_up_shift>=init['spillsize']) or np.any(spill_left_shift>=init['spillsize']) or np.any(spill_right_shift>=init['spillsize']):
        spill_down=np.where(spill_down_shift>=init['spillsize'],spill_down_shift,0)
        spill_down_indices=(np.asarray(np.where(spill_down!=0)))
        spill_down[(spill_down_indices[0],spill_down_indices[1])]=-1
        spill_down[(spill_down_indices[0]+1,spill_down_indices[1])]=1

        spill_up=np.where(spill_up_shift>=init['spillsize'],spill_up_shift,0)
        spill_up_indices=(np.asarray(np.where(spill_up!=0)))
        spill_up[(spill_up_indices[0],spill_up_indices[1])]=-1
        spill_up[(spill_up_indices[0]-1,spill_up_indices[1])]=1
        
        spill_left=np.where(spill_left_shift>=init['spillsize'],spill_left_shift,0)
        spill_left_indices=(np.asarray(np.where(spill_left!=0)))
        spill_left[(spill_left_indices[0],spill_left_indices[1])]=-1
        spill_left[(spill_left_indices[0],spill_left_indices[1]-1)]=1
        
        spill_right=np.where(spill_right_shift>=init['spillsize'],spill_right_shift,0)
        spill_right_indices=(np.asarray(np.where(spill_right!=0)))
        spill_right[(spill_right_indices[0],spill_right_indices[1])]=-1
        spill_right[(spill_right_indices[0],spill_right_indices[1]+1)]=1
        
        a = a+spill_down+spill_up+spill_left+spill_right
        
        shift=spill_shift(init,a)
#        D=np.insert(a,[-1],np.zeros((1,init['size'])),axis=0)
#        D=np.delete(D,0,axis=0)
#        U=np.insert(a,[0],np.zeros((1,init['size'])),axis=0)
#        U=np.delete(U,-1,axis=0)
#        L=np.insert(a,0,0,axis=1)
#        L=np.delete(L,-1,1)
#        R=(np.insert(a,-1,0,axis=1))
#        R=np.delete(R,0,1)
#        spill_down_shift=a-D
#        spill_up_shift=a-U
#        spill_left_shift=a-L
#        spill_right_shift=a-R
        
#    while init['spillsize']+1 in a:
#        indices = np.asarray(np.where(a==init['spillsize']+1))
#        a[a>init['spillsize']]=0
##        Finding indices of spill-over elements, up, down, right, left
#        row_centre=indices[0]
#        row_down=[x+1 for x in indices[0]]
#        row_up=[x-1 for x in indices[0]]
#        col_centre=indices[1]
#        col_right=[y+1 for y in indices[1]]
#        col_left=[y-1 for y in indices[1]]
##        Add one to cell up
#        a[(row_up,col_centre)] = a[(row_up,col_centre)]+1
##        Add one to cell down
#        a[(row_down,col_centre)] = a[(row_down,col_centre)]+1
##        Add one to cell left
#        a[(row_centre,col_left)] = a[(row_centre,col_left)]+1
##        Add one to cell right
#        a[(row_centre,col_right)] = a[(row_centre,col_right)]+1
        
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
    
    #    Creating shifted matrices
    shift=spill_shift(init,a)
#    D=np.insert(a,[-1],np.zeros((1,init['size'])),axis=0)
#    D=np.delete(D,0,axis=0)
#    U=np.insert(a,[0],np.zeros((1,init['size'])),axis=0)
#    U=np.delete(U,-1,axis=0)
#    L=np.insert(a,0,0,axis=1)
#    L=np.delete(L,-1,1)
#    R=(np.insert(a,-1,0,axis=1))
#    R=np.delete(R,0,1)
#    spill_down_shift=a-D
#    spill_up_shift=a-U
#    spill_left_shift=a-L
#    spill_right_shift=a-R
    
    while np.any(spill_down_shift>=init['spillsize']) or np.any(spill_up_shift>=init['spillsize']) or np.any(spill_left_shift>=init['spillsize']) or np.any(spill_right_shift>=init['spillsize']):
        spill_down=np.where(spill_down_shift>=init['spillsize'],spill_down_shift,0)
        spill_down_indices=(np.asarray(np.where(spill_down!=0)))
        spill_down[(spill_down_indices[0],spill_down_indices[1])]=-1
        spill_down[(spill_down_indices[0]+1,spill_down_indices[1])]=1

        spill_up=np.where(spill_up_shift>=init['spillsize'],spill_up_shift,0)
        spill_up_indices=(np.asarray(np.where(spill_up!=0)))
        spill_up[(spill_up_indices[0],spill_up_indices[1])]=-1
        spill_up[(spill_up_indices[0]-1,spill_up_indices[1])]=1
        
        spill_left=np.where(spill_left_shift>=init['spillsize'],spill_left_shift,0)
        spill_left_indices=(np.asarray(np.where(spill_left!=0)))
        spill_left[(spill_left_indices[0],spill_left_indices[1])]=-1
        spill_left[(spill_left_indices[0],spill_left_indices[1]-1)]=1
        
        spill_right=np.where(spill_right_shift>=init['spillsize'],spill_right_shift,0)
        spill_right_indices=(np.asarray(np.where(spill_right!=0)))
        spill_right[(spill_right_indices[0],spill_right_indices[1])]=-1
        spill_right[(spill_right_indices[0],spill_right_indices[1]+1)]=1
        
        a = a+spill_down+spill_up+spill_left+spill_right
        
        shift=spill_shift(init,a)
#        D=np.insert(a,[-1],np.zeros((1,init['size'])),axis=0)
#        D=np.delete(D,0,axis=0)
#        U=np.insert(a,[0],np.zeros((1,init['size'])),axis=0)
#        U=np.delete(U,-1,axis=0)
#        L=np.insert(a,0,0,axis=1)
#        L=np.delete(L,-1,1)
#        R=(np.insert(a,-1,0,axis=1))
#        R=np.delete(R,0,1)
#        spill_down_shift=a-D
#        spill_up_shift=a-U
#        spill_left_shift=a-L
#        spill_right_shift=a-R
        
#        Get avalanche sizes for histogram
#        avalanche_sizes.append(len(indices[0])) 
        
#    while init['spillsize']+1 in a:
#        indices = np.asarray(np.where(a==init['spillsize']+1))
##       Get avalanche sizes for histogram
#        avalanche_sizes.append(len(indices[0])) 
#        a[a>init['spillsize']]=0
##        Finding indices of spill-over elements, up, down, right, left
#        row_centre=indices[0]
#        row_down=[x+1 for x in indices[0]]
#        row_up=[x-1 for x in indices[0]]
#        col_centre=indices[1]
#        col_right=[y+1 for y in indices[1]]
#        col_left=[y-1 for y in indices[1]]
##        Add one to cell up
#        a[(row_up,col_centre)] = a[(row_up,col_centre)]+1
##        Add one to cell down
#        a[(row_down,col_centre)] = a[(row_down,col_centre)]+1
##        Add one to cell left
#        a[(row_centre,col_left)] = a[(row_centre,col_left)]+1
##        Add one to cell right
#        a[(row_centre,col_right)] = a[(row_centre,col_right)]+1
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