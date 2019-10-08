# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:55:09 2019

@author: Kelvin
"""

import numpy as np

def spill_shift(init,a):
    D=np.insert(a,[-1],np.zeros((1,init['size'])),axis=0)
    D=np.delete(D,0,axis=0)
    U=np.insert(a,[0],np.zeros((1,init['size'])),axis=0)
    U=np.delete(U,-1,axis=0)
    L=np.insert(a,0,0,axis=1)
    L=np.delete(L,-1,1)
    R=(np.insert(a,-1,0,axis=1))
    R=np.delete(R,0,1)
    shift={'down':a-D,'up':a-U,'left':a-L,'right':a-R}
    return shift
    
def grid_shift(init,shift,a):
        spill_down=np.where(shift['down']>=init['spillsize'],shift['down'],0)
        spill_down_indices=(np.asarray(np.where(spill_down!=0)))
        spill_down[(spill_down_indices[0],spill_down_indices[1])]=-1
        spill_down[(spill_down_indices[0]+1,spill_down_indices[1])]=1

        spill_up=np.where(shift['up']>=init['spillsize'],shift['up'],0)
        spill_up_indices=(np.asarray(np.where(spill_up!=0)))
        spill_up[(spill_up_indices[0],spill_up_indices[1])]=-1
        spill_up[(spill_up_indices[0]-1,spill_up_indices[1])]=1
        
        spill_left=np.where(shift['left']>=init['spillsize'],shift['left'],0)
        spill_left_indices=(np.asarray(np.where(spill_left!=0)))
        spill_left[(spill_left_indices[0],spill_left_indices[1])]=-1
        spill_left[(spill_left_indices[0],spill_left_indices[1]-1)]=1
        
        spill_right=np.where(shift['right']>=init['spillsize'],shift['right'],0)
        spill_right_indices=(np.asarray(np.where(spill_right!=0)))
        spill_right[(spill_right_indices[0],spill_right_indices[1])]=-1
        spill_right[(spill_right_indices[0],spill_right_indices[1]+1)]=1
        
        a = a+spill_down+spill_up+spill_left+spill_right        
        return a