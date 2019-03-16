# -*- coding: utf-8 -*-
"""
Created on Tue Mar 5 15:49:22 2019

@author: Saloni Rawat
"""

##
##
#Code from the following link
#https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html
##
##
# Globals
import play
import connect4

Players = (connect4.PIECE_ONE, connect4.PIECE_TWO)
History = []
Board   = connect4.create_board()
#Radius  = 40
Winner  = None
Tries   = 0
Mode = 0#input("Select AI (D)efense vs (A)gressive: ")
#print(Mode)
# Game Loop 

while not Winner:
    turn = len(History)

    if turn % 2 == 0:
        print ("Player 1 turn")
        move = play.HumanPlayer(Board, History, Players)   # Player One
        
        #drop piece to column
        
    else:
        print("Player 2 turn")
        #print ("move", move)
        #connect4.print_board(Board)
        move = play.RandomPlayer(Board, History, Players, move, Mode)  # Player Two

    if connect4.drop_piece(Board, move, Players[turn % 2]):
        #print ("drop piece")
        Tries = 0
        History.append(move)

    if Tries > 3:
        print ('Player {} is stuck!'.format((turn % 2) + 1))
        break

    connect4. clear_output()
    connect4.print_board(Board)
    print()
    print()

    connect4.time.sleep(1)

    Winner = connect4.find_winner(Board)

print ('The Winner is {}'.format(connect4.PIECE_COLOR_MAP[Winner]))