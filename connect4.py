# -*- coding: utf-8 -*-
"""
Created on Tue Mar 5 15:44:19 2019

@author: Saloni Rawat
"""
##
##
#Code from the following link
#https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html
##
##


from IPython.display import display, HTML, clear_output
import random
import time

# Game Constants

ROWS       = 7
COLUMNS    = 6

PIECE_NONE = ' '
PIECE_ONE  = 'x'
PIECE_TWO  = 'o'

PIECE_COLOR_MAP = {
    PIECE_NONE : '',
    PIECE_ONE  : 'Player 1',
    PIECE_TWO  : 'Player 2',
}

DIRECTIONS = (
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
)

# Board Functions

def create_board(rows=ROWS, columns=COLUMNS):
    ''' Creates empty Connect 4 board '''
    board = []

    for row in range(rows):
        board_row = []
        for column in range(columns):
            board_row.append(PIECE_NONE)
        board.append(board_row)

    return board

  # Copy board

def copy_board(board):
      ''' Return a copy of the board '''
      rows    = len(board)
      columns = len(board[0])
      copied  = create_board(rows, columns)

      for row in range(rows):
          for column in range(columns):
              copied[row][column] = board[row][column]
      return copied

def print_board(board):
    ''' Prints Connect 4 board '''
    for row in board:
        print ('|' + '|'.join(row) + '|')

def drop_piece(board, column, piece):
    ''' Attempts to drop specified piece into the board at the
    specified column

    If this succeeds, return True, otherwise return False.
    '''
    #print ("board", board, "column", column, "piece", piece)
    col = int(column)
    for row in reversed(board):
        if row[col] == PIECE_NONE:
            row[col] = piece
            return True

    return False

def find_winner(board, length=4):
    ''' Return whether or not the board has a winner '''

    rows    = len(board)
    columns = len(board[0])

    for row in range(rows):
        for column in range(columns):
            if board[row][column] == PIECE_NONE:
                continue

            if check_piece(board, row, column, length):
                return board[row][column]

    return None

def check_piece(board, row, column, length):
    ''' Return whether or not there is a winning sequence starting from
    this piece
    '''
    
    ##insert a check for diagonal
    rows    = len(board)
    columns = len(board[0])

    for dr, dc in DIRECTIONS:
        found_winner = True

        for i in range(1, length):
            r = row + dr*i
            c = column + dc*i

            if r not in range(rows) or c not in range(columns):
                found_winner = False
                break

            if board[r][c] != board[row][column]:
                found_winner = False
                break

        if found_winner:
            return True

    return False

# HTML/SVG Functions

#def display_html(s):
#    ''' Display string as HTML '''
#    display(HTML(s))

#def create_board_svg(board, radius):
#    ''' Return SVG string containing graphical representation of board '''
#
#    rows     = len(board)
#    columns  = len(board[0])
#    diameter = 2*radius
#
#    svg  = '<svg height="{}" width="{}">'.format(rows*diameter, columns*diameter)
#    svg += '<rect width="100%" height="100%" fill="blue"/>'
#
#    for row in range(rows):
#        for column in range(columns):
#            piece = board[row][column]
#            color = PIECE_COLOR_MAP[piece]
#            cx    = column*diameter + radius
#            cy    = row*diameter + radius
#            svg += '<circle cx="{}" cy="{}" r="{}" fill="{}"/>'.format(cx, cy, radius*.75, color)
#
#    svg += '</svg>'
#
#    return svg