# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:55:35 2019

@author: Kelvin
"""

def spill(init,a,indices):
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
    return a