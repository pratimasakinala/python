from random import randint
import math

board = []
for x in range(10) :
    board.append(["O"] * 10)

def print_board(board) :
    for row in board :
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 2)

ship_row = random_row(board)
ship_col = random_row(board)

ship_location = [[[ship_row, ship_col], [ship_row + 1, ship_col]],
                [[ship_row, ship_col + 1], [ship_row + 1, ship_col + 1]]]

# print(ship_row)
# print(ship_col)
print(ship_location)

turns = math.floor(len(board) / 2)

for turn in range(turns) :
    print("Turn", turn + 1)
    try :
        guess_row = int( input('Guess Row: '))
        try :
            guess_col = int( input('Guess Col: '))

            if (guess_row == ship_location[0][0][0] or guess_row == ship_location[0][1][0]) and (guess_col == ship_location[0][0][1] or guess_col == ship_location[1][1][1]) :
                print("I'm hit!")
                count = 0
                board[guess_row][guess_col] = 'X'

                for coords in ship_location:
                    # print('Inside first for loop')
                    for loc in coords:
                        # print('Inside second for loop')
                        if board[loc[0]][loc[1]] == 'X':
                            # print('incrementing count')
                            count += 1

                if count == 4:
                    print("Congratulations! You sunk my battleship!")
                    break
            else:
                if (guess_row < 0 or guess_row > (len(board) - 1)) or (guess_col < 0 or guess_col > (len(board) - 1)) :
                    print("Oops, that's not even in the ocean.")
                elif board[guess_row][guess_col] == "X" :
                    print("You guessed that one already")
                else :
                    print("You missed my battleship!")
                    board[guess_row][guess_col] = "X"

            print_board(board)
        except ValueError :
            print("That's not even a location.")
    except ValueError :
        print("That's not even a location.")

    if turn == turns - 1 :
        print("Game Over")
