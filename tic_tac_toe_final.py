main_board = [" "]*9

dic = dict(q=0,w=1,e=2,a=3,s=4,d=5,z=6,x=7,c=8)


# DISPLAY TIC TAC TOE BOARD 

def display_board():
    print(main_board[dic["q"]] + "  | " + main_board[dic["w"]] + " |  " + main_board[dic["e"]])
    print("---|---|---")
    print(main_board[dic["a"]] + "  | " + main_board[dic["s"]] + " |  " + main_board[dic["d"]])
    print("---|---|---")
    print(main_board[dic["z"]] + "  | " + main_board[dic["x"]] + " |  " + main_board[dic["c"]])



# PLAYER CHOICE PART

def player_choice():
    player1 = " " 
    player2 = " " 

    # while player1 != "X" or player1 != "O":         # W R O N G(this will always give false so loop will never end)
    while player1 not in ("X","O"):
        print("")
        player1 = input("Hey! Player 1, choose your symbol ( X or O ) : ").upper()

        
        if player1 == "X":
           player2 = "O"
           print("")
           print("Player 2, your symbol is O")
           return player1, player2 
        elif player1 == "O":
           player2 = "X"
           print("")
           print("Player 2, your symbol is X")
           return player1, player2
        else:
            print("")
            print("Sorry, that's an invalid choice. \nPlease enter 'X' or 'O'.")





# WIN CHECK PART 

def win_checks(current_player):


    # Horizontal

    if (main_board[dic["q"]] == current_player and
        main_board[dic["w"]] == current_player and
        main_board[dic["e"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True

    if (main_board[dic["a"]] == current_player and
        main_board[dic["s"]] == current_player and
        main_board[dic["d"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True

    if (main_board[dic["z"]] == current_player and
        main_board[dic["x"]] == current_player and
        main_board[dic["c"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True


    # Vertical

    if (main_board[dic["q"]] == current_player and
        main_board[dic["a"]] == current_player and
        main_board[dic["z"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True

    if (main_board[dic["w"]] == current_player and
        main_board[dic["s"]] == current_player and
        main_board[dic["x"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True

    if (main_board[dic["e"]] == current_player and
        main_board[dic["d"]] == current_player and
        main_board[dic["c"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True


    # Diagonal

    if (main_board[dic["q"]] == current_player and
        main_board[dic["s"]] == current_player and
        main_board[dic["c"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True

    if (main_board[dic["e"]] == current_player and
        main_board[dic["s"]] == current_player and
        main_board[dic["z"]] == current_player):
        print(f"Player {current_player} has won this match.")
        return True

    return False





# POSITION CHOICE PART


def position_choice(players):
    
    player1, player2 = players
    current_player = player1
    board = main_board
    # print(board,"\n",track)
    while " " in board:
            
      if current_player == player1:

            print("") 
            position_input = input(f"Player 1 ({player1}), choose a position (Q, W, E, A, S, D, Z, X, C): ").lower()     
            print("") 
            if position_input not in dic:
             print("Invalid position. Please enter one of: Q, W, E, A, S, D, Z, X, or C.")
             continue 
          
            if board[dic[position_input]] == " ":
             board[dic[position_input]] = player1
             display_board()
             if win_checks(player1):
                break
             
             current_player = player2
      
            else:
             print(f"{board[dic[position_input]]} is already at {position_input.upper()}. Please choose another position.")


      else:

          print("")
          position_input = input(f"Player 2 ({player2}), choose a position (Q, W, E, A, S, D, Z, X, C): ").lower()
          print("")
          if position_input not in dic:
             print("Invalid position. Please enter one of: Q, W, E, A, S, D, Z, X, C.")
             continue 
          
          if board[dic[position_input]] == " ":
             board[dic[position_input]] = player2
             display_board()
             if win_checks(player2):
                break
             current_player = player1
             
          else:
             print(f"{board[dic[position_input]]} is already at {position_input.upper()}. Please choose another position.")

      # print(board)
      # print(board.count(" "))
    else:
       print("")
       print("It's a draw, Game over.")
   



# CLEAR BOARD

def clear_board():
    for i in range(len(main_board)):
        main_board[i] = " "
        



# ASKING PLAYER TO CONTINUE PLAYING

def keep_playing():

    ask = " "

    while ask not in ("Y", "N"):
        print("")
        ask = input("Would you like to play another match? (Y/N): ").upper()
        print("")

        if ask == "Y":
            clear_board()
            return True
        elif ask == "N":
            return False
        else:
            print("Invalid input. Please enter Y for Yes or N for No.")





# FINAL PART

main_board = [" "]*9

dic = dict(q=0,w=1,e=2,a=3,s=4,d=5,z=6,x=7,c=8)

play = True

print("")
print("WELCOME TO THE TIC-TAC-TOE GAME!")
print("")
while play:

    display_board()

    players = player_choice()

    position_choice(players)
    
    play = keep_playing()


print("")
print("Thanks for playing Tic-Tac-Toe, See you next time!!")
print("")
print(" ~ ~ ")
print("")



