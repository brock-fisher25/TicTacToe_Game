def update_board(array):
    board = array[0][0].center(3) + "|" + array[0][1].center(3) + "|" + array[0][2].center(3) + "\n --------- \n" + array[1][0].center(3) + "|" + array[1][1].center(3) + "|" + array[1][2].center(3) + "\n --------- \n" + array[2][0].center(3) + "|" + array[2][1].center(3) + "|" + array[2][2].center(3)
    print(board)

def check_horizontal(array):
    symbol = ""
    has_won = False
    for i in range(len(array)):
        symbol = array[i][0]
        for j in range(1,len(array[i])):
            if symbol == "" or array[i][j] != symbol:
                break
            if j == 2:
                has_won = True
                break
    return has_won
            
def check_vertical(array):
    transposed_matrix = [["","",""],["","",""],["","",""]]
    for i in range(len(array)):
        for j in range(len(array[i])):
            transposed_matrix[j][i] = array[i][j]
    return check_horizontal(transposed_matrix)

def check_diagonal(array):
    if array[0][0] == array[1][1] and array[0][0] == array[2][2] and array[0][0] != "":
        return True
    if array[2][0] == array[1][1] and array[2][0] == array[0][2] and array[2][0] != "":
        return True
    return False

def check_win(array):
    return check_horizontal(array) or check_vertical(array) or check_diagonal(array)

def check_board(array, move):
    counter = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if counter == move:
                if array[i][j] != "":
                    return False
                return True
            counter += 1

def update_array(array, move, symbol):
    counter = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if counter == move:
                if array[i][j] != "":
                    return array
                array[i][j] = symbol
                return array
            counter += 1

def play_game():
    player_one = input("Enter player one's name: ")
    player_two = input("Enter player two's name: ")
    has_won = False
    player_one_turn = True
    symbol = ""
    num_moves = 0
    array = [["","",""],["","",""],["","",""]]
    while not has_won:
        if player_one_turn:
            symbol = "X"
            print(player_one + ", your turn (you are X's)")
        else:
            symbol = "O"
            print(player_two + ", your turn (you are O's)")
        move = int(input("Please type in where you'd like to move (From 1-9, 1 is top left corner, 9 is bottom right corner): ")) - 1
        if not check_board(array, move):
            print("You can't move there someone else has already taken that space!")
            continue
        array = update_array(array, move, symbol)
        update_board(array)
        player_one_turn = not player_one_turn
        num_moves += 1
        if check_win(array):
            has_won = True
            if symbol == "O":
                print(player_two + " has won!")
            else:
                print(player_one + " has won!")
            print("To play again, rerun the program!")
            print()
        if num_moves == 9:
            print("It is a tie! Well fought Champions!")
            print("To play again, rerun the program!")
            print()

if __name__ == '__main__':
    play_game()