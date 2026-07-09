"""
Tic-Tac-Toe Game - Python
"""



# GAME BOARD 

main_board = [" "]*9

positions = dict(q=0,w=1,e=2,a=3,s=4,d=5,z=6,x=7,c=8)


# DISPLAY TIC TAC TOE BOARD 

def display_board():
    print(main_board[positions["q"]] + "  | " + main_board[positions["w"]] + " |  " + main_board[positions["e"]])
    print("---|---|---")
    print(main_board[positions["a"]] + "  | " + main_board[positions["s"]] + " |  " + main_board[positions["d"]])
    print("---|---|---")
    print(main_board[positions["z"]] + "  | " + main_board[positions["x"]] + " |  " + main_board[positions["c"]])



# PLAYER SYMBOL SELECTION

def player_symbol():
    player1 = "" 
    player2 = "" 

    while player1 not in ("X","O"):
        print()
        player1 = input("Hey! Player 1, choose your symbol ( X or O ) : ").upper()

        
        if player1 == "X":
           player2 = "O"
           print()
           print("Player 2, your symbol is O")
           return player1, player2 
        elif player1 == "O":
           player2 = "X"
           print()
           print("Player 2, your symbol is X")
           return player1, player2
        else:
            print()
            print("Sorry, that's an invalid choice. \nPlease enter 'X' or 'O'.")





# CHECK WINNING COMBINATIONS

def win_check(current_player):

    # All winning positions
    wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),(0, 3, 6), (1, 4, 7), (2, 5, 8),(0, 4, 8), (2, 4, 6))

    for a,b,c in wins:
        if main_board[a] == main_board[b] == main_board[c] == current_player:
             print(f"Player {current_player} has won this match.")
             return True

    return False
        


# HANDLE PLAYER MOVES

def play_match(players):
    
    player1, player2 = players
    current_player = player1

    while " " in main_board:
            
      if current_player == player1:

            print() 
            position_input = input(f"Player 1 ({player1}), choose a position (Q, W, E, A, S, D, Z, X, C): ").lower()     
            print() 
            if position_input not in positions:
             print("Invalid position. Please enter one of: Q, W, E, A, S, D, Z, X, or C.")
             continue 
          
            if main_board[positions[position_input]] == " ":
             main_board[positions[position_input]] = player1
             display_board()
             if win_check(player1):
                break
             
             current_player = player2
      
            else:
             print(f"{main_board[positions[position_input]]} is already at {position_input.upper()}. Please choose another position.")


      else:

          print()
          position_input = input(f"Player 2 ({player2}), choose a position (Q, W, E, A, S, D, Z, X, C): ").lower()
          print()
          if position_input not in positions:
             print("Invalid position. Please enter one of: Q, W, E, A, S, D, Z, X, C.")
             continue 
          
          if main_board[positions[position_input]] == " ":
             main_board[positions[position_input]] = player2
             display_board()
             if win_check(player2):
                break
             current_player = player1
             
          else:
             print(f"{main_board[positions[position_input]]} is already at {position_input.upper()}. Please choose another position.")

    
    else:
       print()
       print("It's a draw, Game over.")
   



# RESET THE GAME BOARD

def reset_board():
    for i in range(len(main_board)):
        main_board[i] = " "
        



# ASKING PLAYER TO CONTINUE PLAYING

def play_again():

    choice = " "

    while choice not in ("Y", "N"):
        print()
        choice = input("Would you like to play another match? (Y/N): ").upper()
        print()

        if choice == "Y":
            reset_board()
            return True
        elif choice == "N":
            return False
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")





# START THE GAME

play = True

print()
print("WELCOME TO TIC-TAC-TOE GAME!")
print()

print("Board Positions:")
print(" Q | W | E")
print("-----------")
print(" A | S | D")
print("-----------")
print(" Z | X | C")
print()

while play:

    display_board()

    players = player_symbol()

    play_match(players)
    
    play = play_again()


print()
print("Thanks for playing Tic-Tac-Toe! See you next time!")
print()
print(" ~ ~ ")
print()
