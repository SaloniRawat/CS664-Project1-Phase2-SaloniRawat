# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 15:45:05 2019

@author: Saloni Rawat
"""
##
##
#Code from the following link
#https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html
##
##

from numpy import random
import connect4
from evaluate import Evaluator

gameBoard = connect4.create_board()
connect4.print_board(gameBoard)

ev = Evaluator()

def HumanPlayer(board, history, players):
    ''' Read move from human player '''
    columns = len(board[0])
    column  = -1
    #print("columns", columns)

    while column not in range(0, columns):
        column = int(input('Which column? '))
        
        #Handle the exception
        
        if column not in range(0, columns):
            print ("invalid value")
        else: 
            break;
    
        
        
    print("column", column)
        

    return column

def RandomPlayer(board, history, players, oppMove, mode):
    ''' Randomly select a column '''
    #columns = len(board[0])
    #print ("oppMove", oppMove)
    move = -1
    max = 0
    #if mode.lower() == 'd':
           
        #MinMax minmax algorithm
    ev1 = Evaluator.evaluate(ev, oppMove, board)
    #print("ev1", ev1)
 
    for i in ev1:
        row = int(i / 6)
        col = i % 6
        
        if board[row][col] == connect4.PIECE_NONE:
            move = col
                
                
    #elif mode.lower() == 'a'
        
        
        
    return move



