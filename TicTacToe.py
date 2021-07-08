""" TIC TAC TOE """

import math

game_board=['1','2','3',
            '4','5','6',
            '7','8','9']

list_len = len(game_board)

def CheckWinner(game_state):
    #Column check
    for column in range(3):
        if game_state[column] == 'X' and game_state[column+3] == 'X' and game_state[column+6] == 'X':
            return 1
        elif game_state[column] == 'O' and game_state[column+3] == 'O' and game_state[column+6] == 'O':
            return -1

    #Row check
    row=0
    while row<=6:
        if game_state[row] == 'X' and game_state[row+1] == 'X' and game_state[row+2] == 'X':
            return 1
        elif game_state[row] == 'O' and game_state[row+1] == 'O' and game_state[row+2] == 'O':
            return -1
        row+=3

    
    #Diagonal check
    diagonal = 0
    while diagonal <=2:
        if diagonal == 0:
            position = 4
        else:
            position = 2
        if game_state[diagonal] == 'X' and game_state[diagonal+position] == 'X' and game_state[diagonal+(position*2)] == 'X':
            return 1
        elif game_state[diagonal] == 'O' and game_state[diagonal+position] == 'O' and game_state[diagonal+(position*2)] == 'O':
            return -1
        diagonal+=2
        
    return 0
        
def AI():
    best_score= -math.inf
    best_move=''
    #make move
    for i in range(1,10):
        if str(i) not in used_positions:
            game_board[i-1]='X'
            used_positions.append(str(i))
            score = MiniMax(0,False)
            used_positions.remove(str(i))
            game_board[i-1]=str(i)
            if score > best_score:
                best_score = score
                best_move=str(i)
    return best_move
    

def MiniMax(depth,isMaximizing):
    result = CheckWinner(game_board)
    if CheckWinner(game_board) != 0:
        return result

    if isMaximizing:    
        best_score = -math.inf

        #make move
        for m in range(1,10):
            if str(m) not in used_positions:
                game_board[m-1]='X'
                used_positions.append(str(m))
                score = MiniMax(depth+1,False)
                used_positions.remove(str(m))
                game_board[m-1]=str(m)
                if score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = +math.inf

        #make move
        for m in range(1,10):
            if str(m) not in used_positions:
                game_board[m-1]='O'
                used_positions.append(str(m))
                score = MiniMax(depth+1,True)
                used_positions.remove(str(m))
                game_board[m-1]=str(m)
                if score < best_score:
                    best_score = score
        return best_score

running = True
player_turn = True #true = AI false = player
used_positions=[]
turn_counter=0

def DisplayGame(board):
    for board_pos in range(list_len):
        if (board_pos+1)%3 ==0:           #This will print the last value of each row of the game_board then ensure
            print(game_board[board_pos]) #the next value starts on a new line
        else:
            print(game_board[board_pos],end='')

DisplayGame(game_board)

while running:
    if player_turn == True:
        print('Player 1 turn.')
        while True:
            position=AI()
            if position.isnumeric() == True and position not in used_positions:
                pos = game_board.index(position)
                game_board[pos] = 'X'
                used_positions.append(position)
                break
            else:
                print('Invalid value. Please Try again')

        player_turn = False
        
    elif player_turn == False:
        print('Player 2 turn.')
        while True:
            print('Enter the position number and then value')
            position=input()
            if position.isnumeric() ==True and position not in used_positions:
                pos = game_board.index(position)
                game_board[pos]='O'
                used_positions.append(position)
                break
            else:
                print('Invalid value. Please Try again ')
        
        player_turn = True
    
    DisplayGame(game_board)

    if (CheckWinner(game_board))==1:
            print('Player 1 WINS!')
            running = False
    elif (CheckWinner(game_board))==-1:
        print('Player 2 WINS!')
        running = False

    if turn_counter == 8:
        print('TIE!')
        running=False
    turn_counter+=1