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


def get_input(data, duplicate_guess):
    # Set default prompt
    prompt_text = "What is the name of a state?"
    if duplicate_guess:
        # If previous guess was a duplicate, inform user.
        prompt_text = "You've already guessed that state. Try again."

    # Get the user's guess.
    user_input = screen.textinput(title=f"Guess the State [{points}/50]", prompt=prompt_text).title()

    if user_input in data:
        # State guessed is present in db.
        if not data[user_input]["added"]:
            # State guessed has already been guessed previously.
            data[user_input]["added"] = True
            return CORRECT, user_input
        else:
            # Handle states that have already been correctly guessed.
            return DUPLICATE, user_input
    else:
        # Handle incorrectly guessed state.
        return INCORRECT, user_input


def add_state_label(state, data):
    """Shows text with the name of the state at the coordinates provided.

    Parameters
    __________
    state: string
        String containing the name of a state in Title Case
    data: dict
        Dict containing the states and x,y coordinates."""
    labeler = turtle.Turtle()
    labeler.penup()
    labeler.hideturtle()
    labeler.goto(data[state]["x"], data[state]["y"])
    labeler.write(state, False, "center", ("Arial", 8, "normal"))


is_duplicate = False
screen = setup_game_window()
import_state_data(state_data)
while True:
    result, guessed_state = get_input(state_data, is_duplicate)
    is_duplicate = False
    if result == CORRECT:
        points += 1
        add_state_label(guessed_state, state_data)
    elif result == DUPLICATE:
        # Inform and re-ask
        is_duplicate = True
        pass
    elif result == INCORRECT:
        # Game Over
        gg = turtle.Turtle()
        gg.penup()
        gg.color("red")
        gg.hideturtle()
        gg.goto(0, -40)
        gg.write(f"Game Over!\n{points}/50 Correct", False, "center", ("Arial", 36, "bold"))
        break


screen.exitonclick()
