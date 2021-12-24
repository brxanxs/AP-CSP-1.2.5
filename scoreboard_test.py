# This is the scoreboard module which will be referenced in the main file

player_two_index = 0


# in winner_name it uses takes in 2 major string "PlayerOne" and "PlayerTwo" so if your win detector sets it equal to "PlayerX" or "PlayerO" for example so everytime "PlayerOne" or "PlayerTwo" shows up just replace it with your versions of it.
# If you want "PlayerOne" to be "PlayerX" then everywhere you see "PlayerOne" change it to "PlayerX"


def load_scoreboard(file_name, player_names, player_scores, player_two_index):
    scoreboard_file = open(file_name, "r")
    for line in scoreboard_file:
        player_score = []
        index = 0
        new_index = 0
        global winner_name

        # TODO 3: read the player score using a for loop
        while line[index] != "\n":

            if winner_name == "PlayerTwo":
                player_score.append(int(line))
                print("player_score beggining is:", player_score)
                player_two_index += 1
            elif winner_name == "PlayerOne":
                player_score.append(int(line) + 1)
                winner_name = ""

            if winner_name != "PlayerTwo":
                player_score.append(int(line))

            index = index + 1

        print("leader score is:", player_score)

        # TODO 4: add the player score to the list
        if winner_name == "PlayerTwo":
            if player_two_index == 2:
                player_scores.append((player_score[new_index]) + 1)
            elif player_two_index != 2:
                player_scores.append(player_score[new_index])
        if winner_name == "":
            player_scores.append(player_score[new_index])
        print(player_scores)
    scoreboard_file.close()


# update scoreboard by inserting the current player and score to the list at the correct position
def update_scoreboard(file_name, player_names, player_scores, current_name, player_score, test_name):
    score_index = 0

    while (score_index < len(player_scores)):

        if (str(player_score) >= str(player_scores[score_index])):
            break
        else:
            score_index = score_index + 1

    # store the latest scoreboard back in the file
    scoreboard_file = open(file_name, "w")  # this mode opens the file and erases its contents for a fresh start
    score_index = 0

    while (score_index < len(player_scores)):
        scoreboard_file.write(str(player_scores[score_index]) + "\n")
        score_index = score_index + 1

    scoreboard_file.close()


# draw scoreboard and display a message to player
def draw_scoreboard(player_names, player_scores, high_scorer, turtle_object, current_score):
    # clear the screen and move turtle object to (-200, 100) to start drawing the scoreboard
    font_setup = ("Arial", 20, "normal")
    turtle_object.clear()
    turtle_object.penup()
    turtle_object.goto(-200, 100)
    turtle_object.hideturtle()
    turtle_object.down()
    score_index = 0

    # loop through the lists and use the same index to display the corresponding name and score, separated by a tab space '\t'

    turtle_object.write(str(1) + "\t" + "Player One" + "\t" + str(player_scores[score_index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
    turtle_object.down()
    score_index = score_index + 1
    turtle_object.write(str(2) + "\t" + "Player Two" + "\t" + str(player_scores[score_index]), font=font_setup)
    turtle_object.penup()
    turtle_object.goto(-200, int(turtle_object.ycor()) - 50)
    turtle_object.down()

    # Display message about player making/not making scoreboard based on high_scorer
    if (other_test_name == "PlayerOne"):
        turtle_object.write("Player One Wins", font=font_setup)
    elif (other_test_name == "PlayerTwo"):
        turtle_object.write("Player Two Wins", font=font_setup)
    else:
        turtle_object.write("No Winner Entered", font=font_setup)