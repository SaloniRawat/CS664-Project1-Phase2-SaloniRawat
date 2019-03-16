# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:31:46 2019

@author: Saloni Rawat
"""

import numpy as np
import connect4
from tables import rev_segments, all_segments

PLAYER1 = 1
PLAYER2 = 2
NONE = 0

PIECE_WEIGHT_MAP = {
    connect4.PIECE_ONE  : PLAYER1,
    connect4.PIECE_TWO  : PLAYER2,
}

array = []
sumList = []
count = 0

class Evaluator(object):
    
    
    

    def evaluate(self, oppMove, board):
        
        #assign weightage
        weights = [1,5,10]
        #count = int(0)
               
        #sum = 0
        #print("board end", board.end)

        #while not Winner:
       # print("rev", rev_segments)
        #print("all", all_segments)
        
        # remove all filled segments from rev
        
        cnt = 0
        for m in range(len(all_segments)):
            occupied = "true"
            for pos1 in all_segments[m]:
                if pos1 != 200:
                    
                    row1 = int(pos1 /6)
                    col1 = pos1 % 6
                    #print(pos1, row1, col1,"|", board[row1][col1], "|" )
                    
                    if board[row1][col1]== connect4.PIECE_NONE:
                        occupied = "false"
                        #print(pos1, row1, col1,"|", board[row1][col1], "|" , occupied)
                #print(all_segments[m], occupied)
            if occupied == "true":
                #print ("sg: ", all_segments[m])
                
                #print ("pop: ", all_segments[cnt])
                all_segments[m] = 200
                #print(all_segments)
        cnt = cnt +1
                    
                    
        
        
        #check each rev segment
        for seg in all_segments:
            #print("Seg", seg)
            #for y in seg:
            count = 0
            sum=0
            #print("seg", seg)
           
                            
            for pos in seg:
                
                if pos== 200:
                    continue
                else:
                    #print("POS", pos)
                    #print("pos", pos)
                    row = int(pos / 6)
                    col = pos % 6
                   # print("row", row)
                   # print("col", col)
                    #check if the opponent has piece
                    #print("board", board[row][col])
                    if board[row][col] == connect4.PIECE_ONE:
                        #print("MATCH P1")
                        #print("count", count)
                        #print("weight", weights[count])
                        #print(weights.index(1))
                        sum = PLAYER1 * weights[count]
                        #print("sum", sum)
                        #sum
                        count=count +1
                    if board[row][col] == connect4.PIECE_TWO:
                        sum = sum + PLAYER2
                
                   # print("added to sumList: " , seg)
                    sumList.append( [seg, sum])
                        
                        
                           
        
        #print ("SumList", sumList)
        max = 0
        #clear the array
        array.clear()
            
        for i in range(len(sumList)):
           # print("array", sumList[i][0], "sum", sumList[i][1])
            temp = sumList[i][0]
            if  temp[1]!=200 and sumList[i][1] > max:
                # find max for all the values first
                max = sumList[i][1]
                #print ("max", max)
        
        for i in sumList:
            
           # print ("SUM LIST:")
            #print(i)
            if  i[0][1] != 200 and i[1] == max:
                #print (i[0][1])
               # print("row", i[0],i[1])
                array.append(i[0])
                
        #print ("Length: ", len(array))
        #print("array:" , array)
#        
#        for i in array:
#            print ("Option: ", i)
        
        if len(array)!=0:
            rand= np.random.randint(0, len(array))
        else:
            print("No possible move")
    
        return array[rand]
        

