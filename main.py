import csv
import turtle

CORRECT = 0
INCORRECT = 1
DUPLICATE = 2
points = 0
state_data = {}


def setup_game_window():
    window = turtle.Screen()
    window.title("US States Game")
    window.setup(width=725, height=491)
    window.addshape("blank_states_img.gif")
    turtle.shape("blank_states_img.gif")
    return window


def import_state_data(data):
    with open("50_states.csv") as data_file:
        csv_entries = csv.reader(data_file)
        for entry in csv_entries:
            # Filter out the column header entry, add the rest.
            if entry[0] != "state":
                data[entry[0]] = {
                    # x,y coordinates on game screen to print label.
                    "x": int(entry[1]),
                    "y": int(entry[2]),
                    # Flag to exclude this state if it has been guessed.
                    "added": False,
                }


def get_input(data):
    user_input = screen.textinput(title="Guess the State", prompt="What is a state name?").title()
    if user_input in data:
        # State guessed is present in db.
        if not data[user_input]["added"]:
            # State guessed has already been guessed previously.
            data[user_input]["added"] = True
            return CORRECT
        else:
            # Handle states that have already been correctly guessed.
            return DUPLICATE
    else:
        # Handle incorrectly guessed state.
        return INCORRECT


screen = setup_game_window()
import_state_data(state_data)
while True:
    result = get_input(state_data)
    if result == CORRECT:
        points += 1
        # Add label
    elif result == DUPLICATE:
        # Inform and re-ask
        pass
    elif result == INCORRECT:
        # Game Over
        break


screen.exitonclick()
