def game_title():
    print("         T I C -- T A C -- T O E -- G A M E      ")
    print("                   FOR 2 PLAYERS                ")
    print("\n")
    print("    |     |    ")
    print(" 1  |  2  |  3 ")
    print("___ | ___ | ___")
    print("    |     |    ")
    print(" 4  |  5  |  6 ")
    print("___ | ___ | ___")
    print("    |     |    ")
    print(" 7  |  8  |  9 ")
    print("    |     |    ")
    print("\n")

def display_board(board):
    print("↓↓↓\n")
    print(f'    |     |    ')
    print(f' {board[1]}  |  {board[2]}  |  {board[3]} ')
    print(f'___ | ___ | ___')
    print(f'    |     |    ')
    print(f' {board[4]}  |  {board[5]}  |  {board[6]} ')
    print(f'___ | ___ | ___')
    print(f'    |     |    ')
    print(f' {board[7]}  |  {board[8]}  |  {board[9]} ')
    print(f'    |     |    ')
    print('\n')

def player_input():
    marker = ''
    x = input("Enter a name for player 1\n→ ")
    o = input("\nEnter a name for player 2\n→ ")
    player2 = ''

    while marker.upper() not in ['X', 'O']:
        marker = input(f"\n{x}, choose X or O\n→ ").upper()

    player1 = marker.upper()
    player2 = 'O' if player1 == 'X' else 'X'

    print('\n' + x + ' → ' + player1 + '\n' + o + ' → ' + player2)
    return player1, player2, x, o

def win_check(board, mark):
    return (
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark)
    )

def player_choice(board, player_name):
    while True:
        try:
            position = int(input(f"{player_name}, Choose a position (1-9): "))
            if position in range(1, 10):
                if board[position] == ' ':
                    return position
                else:
                    print("That position is already taken. Try another one.\n")
            else:
                print("Position must be between 1 and 9.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def game():
    game_title()
    board = [' '] * 10
    player1_marker, player2_marker, name1, name2 = player_input()
    
    turn = 'player1'
    game_over = False

    while not game_over:
        display_board(board)

        if turn == 'player1':
            position = player_choice(board, f"{name1} ({player1_marker})")
            board[position] = player1_marker
            print(f"\nPlaced {player1_marker} at position {position}")
            if win_check(board, player1_marker):
                display_board(board)
                print(f"\n¡{name1} has won!")
                game_over = True
            elif ' ' not in board[1:]:
                display_board(board)
                print("Draw")
                game_over = True
            else:
                turn = 'player2'
                print(f"{name2}, your turn")
        else:
            position = player_choice(board, f"{name2} ({player2_marker})")
            board[position] = player2_marker
            print(f"\nPlaced {player2_marker} at position {position}")
            if win_check(board, player2_marker):
                display_board(board)
                print(f"\n¡{name2} has won!")
                game_over = True
            elif ' ' not in board[1:]:
                display_board(board)
                print("Draw")
                game_over = True
            else:
                turn = 'player1'
                print(f"\n{name1}, your turn")

game()
print(input("Click to finish"))