# -*- coding: utf-8 -*-
"""
Created on Wed Mar 6 10:19:41 2019

@author: Saloni Rawat
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 14:06:37 2019

@author: Saloni Rawat
"""
#
# Segment tables
#
# Segments are quartets of indices that represent four squares aligned and
# consecutive in the board.
# If a segment contains piece of the same player, that player won the game.
#
# all_segments is a 2d array, each row is a segment
# rev_segments is an index square -> group of segments that pass by the square
# code used from https://github.com/duilio/c4
#

import numpy as np
import itertools

#all possible 4-sq combinations that lead to win 
all_segments = []

rev_segments = [[] for x in range(7*6)]

#creates an array and reshapes it into 7*6 - GAMEBOARD Layout
_indices = np.arange(7*6).reshape((7, 6))
    
#print (_indices)

def add_rev(line):
    for x in range(len(line)-3):
        seg = line[x:x+4]
        all_segments.append(seg)
        #consolidates are all arrays of possible 4 sq combinations
        for n in seg:
            rev_segments[n].append(seg)
            #print (rev_segments)
            
# creates column array
for col in _indices:
    #print ("Col: ", col)
    add_rev(col)

#creates row array
for row in _indices.transpose():
    #print ("Row: ", row)
    add_rev(row)

#creates array for diagnols
for idx in (_indices, _indices[:, ::-1]):
    #print ("idx: ", idx)
    for di in range(-7, 7):
       # print ("di: ", di)
        diag = idx.diagonal(di)
       # print("diag", diag)
        add_rev(diag)

# converts 
all_segments = np.asarray(all_segments)
rev_segments = np.asarray([np.asarray(x) for x in rev_segments])

#print ("Updated: " , _indices)
#
#print("all segments" , all_segments)
#print("rev segments" , rev_segments)


