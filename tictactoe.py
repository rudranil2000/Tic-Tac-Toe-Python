# -*- coding: utf-8 -*-
"""
Created on Tue May 19 17:12:53 2020

@author: Rudranil Ghosh

TIC TACK TOE
"""

from os import system, name
#from time import sleep
import random


def clear():
    #input('Press Enter to continue')
    #sleep(2)
    if name=='nt':
        _=system('cls')

def display_board(board):
    
    clear()
    
    print(' '*2+ ' '*2+' |'+' '*2+' '*2+' |')
    print(' '*2+board[7]+' '*2+'|'+ ' '*2+board[8]+' '*2+'|'+' '*2+board[9])
    print(' '*2+ ' '*2+' |'+' '*2+' '*2+' |')
    
    print('-'*17)
    
    print(' '*2+ ' '*2+' |'+' '*2+' '*2+' |')
    print(' '*2+board[4]+' '*2+'|'+ ' '*2+board[5]+' '*2+'|'+' '*2+board[6])
    print(' '*2+ ' '*2+' |'+' '*2+' '*2+' |')
    
    print('-'*17)
    
    print(' '*2+ ' '*2+' |'+' '*2+' '*2+' |')
    print(' '*2+board[1]+' '*2+'|'+ ' '*2+board[2]+' '*2+'|'+' '*2+board[3])
    print(' '*2+ ' '*2+' |'+' '*2+' '*2+' |')

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position]=marker
    
def win_check(board,mark):
    
    for i in [1,2,3]:
        if board[i]==board[i+3]==board[i+6]==mark:
            return True
    for i in [1,4,7]:
        if board[i]==board[i+1]==board[i+2]==mark:
            return True
    if (board[7] == board[5] == board[3] == mark) or (board[9] == board[5] == board[1] == mark):
        return True
    else:
        return False
            
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position]==' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Player 1 won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
                    # Player2's turn.
                    
                    display_board(theBoard)
                    position = player_choice(theBoard)
                    place_marker(theBoard, player2_marker, position)
        
                    if win_check(theBoard, player2_marker):
                        display_board(theBoard)
                        print('Player 2 has won!')
                        game_on = False
                    else:
                        if full_board_check(theBoard):
                            display_board(theBoard)
                            print('The game is a draw!')
                            break
                        else:
                            turn = 'Player 1'
        
    if not replay():
        break
    