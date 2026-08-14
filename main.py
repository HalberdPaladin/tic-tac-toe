board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-',
]

# print board

def printBoard(board):
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])

#get player name

def symbol_and_player_name():
    p1 = input("player 1 name is: ")
    p2 = input("player 2 name is: ")

    print("please choose either 'X' or 'O' as your symbol")
    s1 = input("what will be" + " " + p1 +"'s symbol").upper()
    s2 = input("what will be" + " " + p2 +"'s symbol").upper()

    while s2 == s1:
        s2 = input("plz pick a different symbol for " + p2 + ": ").upper()

    return p1, s1, p2, s2


#get player move

def getplayermove(current_name,current_symbol):
    while True:
        move = input(f"player {current_name},{current_symbol} what move do you want to play?(1-9): ")
        if move.isdigit():
            move=int(move)
            move-=1

            if 0<=move<=8:
                if board[move] == '-':
                    board[move] = current_symbol
                    break

                else:
                    print("That spot is already taken, try again.")

            print("Enter number between 1-9.")

        else:
            print("invalid Input.")

# check winner

def check_Winner(board, symbol):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8], #rows
        [0,3,6],[1,4,7],[2,5,8], #column
        [0,4,8],[2,4,6]         #diagonal
    ]

    for i in win_conditions:
        if board[i[0]] == symbol and board[i[1]] == symbol and board[i[2]] == symbol:
            return True

    return False

# actually draw?

def check_draw(board):
    return '-' not in board

# real part
if __name__ == '__main__':
    print("welcome to tic-tac-toe!\n")

    p1_name, p1_symbol, p2_name, p2_symbol = symbol_and_player_name()
    players = [(p1_name,p1_symbol),(p2_name,p2_symbol)]
    turn=0

    game_running = True

    while game_running:
        current_name, current_symbol = players[turn % 2]

        printBoard(board)
        getplayermove(current_name, current_symbol)

        if check_Winner(board, current_symbol):
            printBoard(board)
            print(f"🎉 Congratulations {current_name}! You win with '{current_symbol}'! 🎉")
            game_running = False
            break

        if check_draw(board):
            printBoard(board)
            print("It's a draw! No empty spaces left.")
            game_running = False
            break

# Increment turn count to switch to the other player next loop
        turn += 1
