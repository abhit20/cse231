##################################################################
#  CSE 231 Project 10
#  Initializes a checkerboard for gameplay
#  If player chooses black, he/she go first
#       First one to go, chooses to skip, hints for next moves, or chooses the piece to move
#       The next one goes
#       If white runs out of move, black wins, and vice versa. If both run out, it ends in a draw
#       Game Ends
####################################################################

import tools
import gameai as ai
from checkers import Piece
from checkers import Board
import examples

"""
    Write something about this program here.
"""

# Indexify goes from numbers and values into tuple with the index
def indexify(position):
    # A list of the letters and numbers to a tuple with both the indexes
    letter_value = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    number_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

    return letter_value.index(position[0]),number_value.index(position[1:])

# Deindexify turns row and col into a number and value
def deindexify(row, col):
    # A list is used to turn row and col into letter_value and number_value
    letter_value = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']
    number_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

    return letter_value[row]+number_value[col]


def initialize(board):
    """
    This function puts white and black pieces according to the checkers
    game positions. The black pieces will be on the top three rows and
    the white pieces will be on the bottom three rows (for an 8x8 board).
    The first row for the black pieces will be placed as a2, a4, a6, ...
    etc. and the next rows will be b1, b3, b5, ... etc. For the white
    rows, the placement patterns will be opposite of those of blacks.
    This must work for any even length board size.
    """
    row = col = board.get_length()
    initrows = (row // 2) - 1
    for r in range(row - 1, row - (initrows + 1), -1):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece('white'))
    for r in range(0, initrows):
        for c in range(0 if r % 2 == 1 else 1, col, 2):
            board.place(r, c, Piece())

# Count_pieces counts the number of black and white pieces on the board
def count_pieces(board):
    # Gets the length (number of columns) of the board
    board_length = board.get_length()
    # Initializes variables to count the white and black pieces
    black_count = 0
    white_count = 0
    # For every row in the board, it does the following
    for row in range(board_length):
        # For every column in the board, it does the following
        for col in range(board_length):
            # Gets the piece at the given row and col
            piece = board.get(row, col)
            # If no piece exists, it passes
            if piece == None:
                pass
            # Else, it does the following
            else:
                # If the piece is black then black count incremented by 1
                if piece.is_black() == True:
                    black_count +=1
                # If the piece is white then white count incremented by 1
                if piece.is_white() == True:
                    white_count +=1

    # Returns a tuple of black and white count
    return black_count,white_count


# Get_all_moves for a color on the board and sort it
def get_all_moves(board, color, is_sorted=False):
    # Gets the length (number of columns) of the board
    board_length = board.get_length()
    # Initializes a lst to be appended to
    lst = []
    # For every row in the board, it does the following
    for row in range(board_length):
        # For every column in the board, it does the following
        for col in range(board_length):
            # Gets the piece at the given row and col
            piece = board.get(row, col)
            # If no piece exists, it passes
            if piece==None:
                pass
            # Else, it does the following
            else:
                # If the color of the piece is equal to color argument
                if piece.color() == color:
                    # This gets the moves of the location
                    c = tools.get_moves(board, row, col, is_sorted)
                    for a in c:
                        # A tuple of current spot and next spot is added to the list
                        lst.append((deindexify(row,col),a))
    # Returns a tuple of current spot and second element is the spot that the piece can make
    return lst


def sort_captures(all_captures, is_sorted=False):
    '''If is_sorted flag is True then the final list will be sorted by the length
    of each sub-list and the sub-lists with the same length will be sorted
    again with respect to the first item in corresponding the sub-list,
    alphabetically.'''

    return sorted(all_captures, key=lambda x: (-len(x), x[0])) if is_sorted \
        else all_captures


# Gets all captures from a function in tools.py
def get_all_captures(board, color, is_sorted=False):
    # Gets the length (number of columns) of the board
    board_length = board.get_length()
    # Initializes a lst to be appended to
    lst = []
    # For every row in the board, it does the following
    for row in range(board_length):
        # For every column in the board, it does the following
        for col in range(board_length):
            # Gets the piece at the given row and col
            piece = board.get(row, col)
            # If no piece exists, it passes
            if piece == None:
                pass
            # Else, it does the following
            else:
                # If the color of the piece is equal to color argument
                if piece.color() == color:
                    # This gets the moves of the location
                    c = tools.get_captures(board, row, col, is_sorted)
                    for a in c:
                        # A list is added to the list
                        lst.append(a)
    # Returns the list
    return lst


# Removes the piece at the current spot and moves it to the given spot, if valid
def apply_move(board, move):
    # Initial_point_index gets the location of the current spot
    initial_piece_index = indexify(move[0])
    # Final_point_index gets the location of the spot to move to
    final_piece_index = indexify(move[1])

    # If the location to move to is empty, then the following code is run
    if board.get(final_piece_index[0],final_piece_index[1]) == None:
        # Piece stores the piece at the given location
        piece = board.get(initial_piece_index[0],initial_piece_index[1])
        # The piece is placed at the next spot
        place_piece = board.place(final_piece_index[0],final_piece_index[1],piece)
        # The piece is removed from its old location
        remove_piece = board.remove(initial_piece_index[0], initial_piece_index[1])

        # If the piece is moved to the first or the last row, the piece becomes
        if (final_piece_index[0] == 0) or (final_piece_index[0] == 7):
            if piece.is_king() == False:
                piece.turn_king()
    else:
        # Raises Exception the move to spot is not equal to None
        raise Exception("Invalid move, please type 'hints' to get suggestions.")

# Removes the piece at the current spot and moves it to the given spot, if valid
def apply_capture(board, capture_path):
    """
    Write something about this function here.

    Raise this exception below:
        raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.")
    If,
        a. there is no jump found from any position in capture_path, i.e. use
            tools.get_jumps() function to get all the jumps from a certain
            position in capture_path
        b. the destination position from a jump is not in the jumps list found
            from tools.get_jumps() function.
    """
    # For the increment to the length of the capture_path-1, the following code runs
    for a in range(len(capture_path) - 1):
        # Initial_piece_index is equal to the current location of the piece
        initial_piece_index = indexify(capture_path[a])
        # Jump_piece_index is equal to the next location of the piece
        jump_piece_index = indexify(capture_path[a + 1])
        # If the jump and capture path[a+1] in the get_jumps(), then the following is run
        if tools.get_jumps(board,initial_piece_index[0], initial_piece_index[1]) and capture_path[a + 1] in tools.get_jumps(board,initial_piece_index[0], initial_piece_index[1]):
            # Piece stores the piece that exists at that position
            piece = board.get(initial_piece_index[0], initial_piece_index[1])
            # Removes the piece at the current location
            board.remove(initial_piece_index[0], initial_piece_index[1])
            # Places the piece at te jump location
            board.place(jump_piece_index[0], jump_piece_index[1], piece)

            # If the jump_piece_index (row) is greater than initial_piece_index (row), row_index is set to initial row+1
            if jump_piece_index[0] > initial_piece_index[0]:
                row_index = initial_piece_index[0] + 1
            # Else row_index is set to initial_row-1
            else:
                row_index = initial_piece_index[0] - 1
            # If the jump_piece_index (col) is greater than initial_piece_index (col), row_index is set to initial col+1
            if jump_piece_index[1] > initial_piece_index[1]:
                column_index = initial_piece_index[1] + 1
            # Else row_index is set to initial_row-1
            else:
                column_index = initial_piece_index[1] - 1

            # Removes the piece at the jump location
            board.remove(row_index, column_index)
            # If piece color is black and jump_piece_index row is equal to board length -1
            # or equal to 0 (top and bottom rows), piece is turned into a king
            if (piece.color == "black" and jump_piece_index[0] == board.get_len() - 1) or (piece.color == "white" and jump_piece_index[0] == 0):
                piece.turn_king
        else:
            # Raises Exception if the jump is invalid
            raise RuntimeError("Invalid jump/capture, please type" \
                               + " \'hints\' to get suggestions.")


# Gives hints on the next valid moves or captures.
def get_hints(board, color, is_sorted=False):
    if get_all_captures(board,color,is_sorted) != []:
        return ([], get_all_captures(board, color, is_sorted))
    else:
        return(get_all_moves(board,color,is_sorted),[])


# Gets the winner of the game
def get_winner(board, is_sorted=False):
    # hints_white stores the hints for white piece from get_hints
    hints_white = get_hints(board,"white",is_sorted)
    # hints_black stores the hints for black piece from get_hints
    hints_black = get_hints(board,"black",is_sorted)
    # If the len of hints_black is zero, white wins
    if (len(hints_black[0]) == 0) and (len(hints_black[1]) == 0):
        return "white"
    # If the len of hints_white is zero, black wins
    elif (len(hints_white[0]) == 0) and (len(hints_white[1]) == 0):
        return "black"
    # If the len of hints_black and hints_white is zero, its a draw
    else:
        return 'draw'


# is_game_finished decides if the game is finished by taking in board and is_sorted
def is_game_finished(board, is_sorted=False):
    # hints_white stores the hints for white piece from get_hints
    hints_white = get_hints(board, "white", is_sorted)
    # hints_black stores the hints for black piece from get_hints
    hints_black = get_hints(board, "black", is_sorted)
    # If the len of the either get_hints for white or black is zero, game is finished (True)
    if ((len(hints_black[0]) == 0) and (len(hints_black[1]) == 0)) or ((len(hints_white[0]) == 0) and (len(hints_white[1]) == 0)):
        return True
    # Else it returns False (game is not finished)
    else:
        return False


# Some error messages to save lines.
move_error = "Invalid move, please type \'hints\' to get suggestions."
hasjump_error = "You have jumps, please type \'hints\' to get suggestions."
jump_error = "Invalid jump, please type \'hints\' to get suggestions."
hint_error = "Invalid hint number."
cmd_error = "Invalid command."


def game_play_human():
    """
    This is the main mechanism of the human vs. human game play.
    Use this function to write the game_play_ai() function.
    """
    # UNCOMMENT THESE TWO LINES TO TEST ON MIMIR SUBMISSION
    # Piece.symbols = ['b', 'w']
    # Piece.symbols_king = ['B', 'W']

    prompt = "[{:s}'s turn] :> "
    print(tools.banner)

    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()

    # Take a board of size 8x8
    board = Board(8)
    initialize(board)

    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")

    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)

            print("Current board:")
            board.display(piece_count)

            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()

            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}" \
                              .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)

    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    # --- end of game play human ---


def game_play_ai():
    """
    This is the main mechanism of the human vs. ai game play. You need to
    implement this function by taking helps from the game_play_human()
    function.

    For a given board situation/state, you can call the ai function to get
    the next best move, like this:

        move = ai.get_next_move(board, turn)

    where the turn variable is a color 'black' or 'white', also you need to
    import ai module as 'import gameai as ai' at the beginning of the file.
    This function will be very similar to game_play_human().
    """
    prompt = "[{:s}'s turn] :> "
    print(tools.banner)

    # Choose the color here
    (my_color, opponent_color) = tools.choose_color()

    # Take a board of size 8x8
    board = Board(8)
    initialize(board)

    # Decide on whose turn, use a variable called 'turn'.
    turn = my_color if my_color == 'black' else opponent_color
    print("Black always plays first.\n")

    # loop until the game is finished
    while not is_game_finished(board):
        try:
            # Count the pieces and assign into piece_count
            piece_count = count_pieces(board)

            print("Current board:")
            board.display(piece_count)

            # Get the command from user using input
            command = input(prompt.format(turn)).strip().lower()

            # Now decide on different commands
            if command == 'pass':
                break
            elif command == 'exit':
                break
            elif command == 'hints':
                (moves, captures) = get_hints(board, turn, True)
                if moves:
                    print("You have moves:")
                    for i, move in enumerate(moves):
                        print("\t{:d}: {:s} --> {:s}" \
                              .format(i + 1, move[0], move[1]))
                if captures:
                    print("You have captures:")
                    for i, path in enumerate(captures):
                        print("\t{:d}: {:s}".format(i + 1, str(path)))
            else:
                command = [s.strip().lower() for s in command.split()]
                (moves, captures) = get_hints(board, turn, True)
                action = None
                if command and command[0] == 'move' and len(command) == 3:
                    if not captures:
                        action = (command[1], command[2])
                        if action in moves:
                            apply_move(board, action)
                        else:
                            raise RuntimeError(move_error)
                    else:
                        raise RuntimeError(hasjump_error)
                elif command and command[0] == 'jump' and len(command) >= 3:
                    action = command[1:]
                    if action in captures:
                        apply_capture(board, action)
                    else:
                        raise RuntimeError(jump_error)
                elif command and command[0] == 'apply' and len(command) == 2:
                    id_hint = int(command[1])
                    if moves and (1 <= id_hint <= len(moves)):
                        action = moves[id_hint - 1]
                        apply_move(board, action)
                    elif captures and (1 <= id_hint <= len(captures)):
                        action = captures[id_hint - 1]
                        apply_capture(board, action)
                    else:
                        raise ValueError(hint_error)
                else:
                    raise RuntimeError(cmd_error + tools.usage)
                print("\t{:s} played {:s}.".format(turn, str(action)))
                turn = my_color if turn == opponent_color else opponent_color
        except Exception as err:
            print("Error:", err)

    # The loop is over.
    piece_count = count_pieces(board)
    print("Current board:")
    board.display(piece_count)
    if command != 'pass':
        winner = get_winner(board)
        if winner != 'draw':
            diff = abs(piece_count[0] - piece_count[1])
            print("\'{:s}\' wins by {:d}! yay!!".format(winner, diff))
        else:
            print("This game ends in a draw.")
    else:
        winner = opponent_color if turn == my_color else my_color
        print("{:s} gave up! {:s} is the winner!! yay!!!".format(turn, winner))
    pass
    # --- end of game play ai ---


def main():
    # Prints the initial banner
    print(tools.banner)

    Piece.symbols = ['b', 'w']
    Piece.symbols_king = ['B', 'W']

    # Choose color
    user_color = input("Pick a color: ")

    # Prints color choices
    if user_color.lower() == "white":
        ai_color = "black"
        print("You are '{}' and your opponent is '{}'.".format(user_color,ai_color))
    else:
        ai_color = "white"
        print("You are '{}' and your opponent is '{}'.".format(user_color, ai_color))
    print("Black always plays first.\n")
    print("Current board:")
    # Prints initial board
    board = Board()
    initialize(board)
    board.display()



# main function, the program's entry point
if __name__ == "__main__":
    main()