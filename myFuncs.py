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
#    shift['down']=a-D
#    shift['up']=a-U
#    shift['left']=a-L
#    shift['right']=a-R
    return shift
#    spill_down_shift=a-D
#    spill_up_shift=a-U
#    spill_left_shift=a-L
#    spill_right_shift=a-R
#    return spill_down_shift,spill_up_shift,spill_left_shift,spill_right_shift