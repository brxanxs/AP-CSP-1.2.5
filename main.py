# main.py
# written, mainly, by Brian Frodelius
# file partner contributions include: manage_leaderboard(), variables under # ~~~module imports~~~
# Note: idea for end condition becoming winner_check() came from
# https://pythonturtle.academy/tic-tac-toe-source-code-included/
import turtle
import board as board
import scoreboard_module as sb

# ~~~variable naming~~~
squares_num = 9
shape_images = ['O.gif', 'X.gif']  # O, X
# List within a list contains a x and y point in the middle of a given square
picture_placement = [[-3.5, 3.5], [0, 3.5], [3.5, 3.5],
                     [-3.5, 0], [0, 0], [3.5, 0],
                     [-3.5, -3.5], [0, -3.5], [3.5, -3.5]]
# List of a list organized in Minimum x, Maximum x, Minimum y, Maximum y ranges
ranges = [[-5, -2, 2, 5], [-2, 2, 2, 5], [2, 5, 2, 5],
          [-5, -2, -2, 2], [-2, 2, -2, 2], [2, 5, -2, 2],
          [-5, -2, -5, -2], [-2, 2, -5, -2], [2, 5, -5, -2]]
# the ranges are arranged so the every 4 numbers are a box and per pair identify
# distance between. e.g. -150, -50 is the distance in x axis from one side to another
current_turn = 'Player_1'  # cannot be changed
player1_turns = []  # used to calculate who won
player2_turns = []
winner = 0

# ~~~module imports~~~
scoreboard_file_name = "scoreboard.txt"
player_names_list = []
player_scores_list = []
wins = 0
current_name = "."
winner = "."
winning_index = 0

# ~~~config~~~
wn = turtle.Screen()
wn.title("Tic-Tac-Toe.py")
wn.setworldcoordinates(-6, -6, 6, 6)  # used for small, more "manageable" numbers
wn.setup(800, 800)
wn.tracer(0, 0)
for i in shape_images:  # installs shapes
    wn.addshape(i)


# ~~~events~~~
def assign_shape():  # creates turtles based on whether the "current_turn" player chose X or O
    global player
    shape_choice = input(str("Options: X, O\nShape for {}: ").format(current_turn))
    if shape_choice == "X" or shape_choice == "x":
        player = turtle.Turtle(shape=shape_images[1])
        print("\nPlayer_2's shape is O\n{}'s shape is X, you go first.".format(current_turn))
    elif shape_choice == "O" or shape_choice == "o":
        player = turtle.Turtle(shape=shape_images[0])
        print("\nPlayer_2's shape is X\n{}'s shape is O, you go first.".format(current_turn))
    else:  # re-runs function if answer isn't one of the options
        print('\nPlease chose a valid option...\n')
        assign_shape()
    player.ht()
    player.penup()
    player.speed(0)


def player_turn(valid_spot):
    global player1_turns, player2_turns
    if valid_spot is True:
        player.goto(picture_placement[index][0], picture_placement[index][1])
        # preset coordinates, in the middle of a square
        player.stamp()
        if current_turn == 'Player_1':  # adds coordinates to a list for duplicate and win detection
            player1_turns.append(index)
        elif current_turn == 'Player_2':
            player2_turns.append(index)
    elif valid_spot is False:
        print('Where you clicked was invalid...\nTry again!')
        player_turn('placeholder')  # placeholder is used to "cancel" and wait on onscreenclick


def change_turn():
    global current_turn
    if player.shape() == shape_images[1]:  # changes shape per "valid" turn
        player.shape(shape_images[0])
    else:
        player.shape(shape_images[1])
    if current_turn == 'Player_1':  # changes name per "valid turn" for lists that depend on names
        current_turn = 'Player_2'  # used later to determine "who" won when displaying the winner
    else:
        current_turn = 'Player_1'


def coord_check(x, y):
    global index
    i = 0
    for index in range(len(ranges)):  # checks if spot clicked is within a box range
        if ranges[index][int(i)] < x < ranges[index][int(i + 1)]:  # "solid" #s used in combination with lists of lists
            if ranges[index][int(i + 2)] < y < ranges[index][int(i + 3)]:
                index = int(index)  # used later in different instances since the loop ends once a valid range is found
                return True


def duplicate_check():
    if index in player1_turns or index in player2_turns:  # e.g. if range[8] is in player#_turns to check for duplicates
        None  # when attempting to use "if index not in player#_turns" there was an error
    else:
        return False


def winner_check(turn):
    if len(player1_turns) > 2 or len(player2_turns) > 2:  # starts checking for winners at 3 turns
        # a little redundant but could not find a better solution
        if 0 in turn and 1 in turn and 2 in turn:  # top row
            return True
        if 3 in turn and 4 in turn and 5 in turn:  # middle row
            return True
        if 6 in turn and 7 in turn and 8 in turn:  # bottom row
            return True
        if 0 in turn and 3 in turn and 6 in turn:  # left column
            return True
        if 1 in turn and 4 in turn and 7 in turn:  # middle column
            return True
        if 2 in turn and 5 in turn and 8 in turn:  # right column
            return True
        if 0 in turn and 4 in turn and 8 in turn:  # diagonal
            return True
        if 2 in turn and 4 in turn and 6 in turn:  # diagonal
            return True


def board_check(x, y):
    global squares_num, winner, player1_turns, player2_turns, current_turn
    global player_scores_list, winner_name
    if coord_check(x, y) is True and duplicate_check() is False:
        player_turn(True)
        if current_turn == 'Player_1':
            if winner_check(player1_turns) is True:  # end game condition
                winner_name = "PlayerOne"
                manage_scoreboard()
        elif current_turn == 'Player_2':
            if winner_check(player2_turns) is True:
                winner_name = "PlayerTwo"
                manage_scoreboard()
        change_turn()
    else:
        player_turn(False)
    if int(len(player1_turns) + len(player2_turns)) == 9:  # ends game if there's no winner
        exit()


def manage_scoreboard():
    global player_scores_list
    global player_names_list
    global wins
    global wn, winner_name
    wn.clearscreen()
    # load all the leaderboard records into the lists
    sb.load_scoreboard(scoreboard_file_name, player_names_list, player_scores_list, winning_index, winner_name)
    scoreboard_writer = turtle.Turtle()
    scoreboard_writer.ht()
    if len(player_scores_list) < 5 or int(wins) > player_scores_list[4]:
        sb.update_scoreboard(scoreboard_file_name, player_names_list, player_scores_list, current_name, wins, winner)
        sb.draw_scoreboard(player_names_list, player_scores_list, True, scoreboard_writer, wins, winner_name)

    else:
        sb.draw_scoreboard(player_names_list, player_scores_list, False, scoreboard_writer, wins, winner_name)


# ~~~event triggering~~~


board.draw_outline()
assign_shape()
wn.onscreenclick(board_check)
wn.mainloop()
