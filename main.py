import csv
import turtle

db = {
    "states": {},
}
screen = turtle.Screen()


def setup_game_window(window):
    window = turtle.Screen()
    window.title("US States Game")
    window.setup(width=725, height=491)
    window.addshape("blank_states_img.gif")
    turtle.shape("blank_states_img.gif")


def import_state_data(data):
    with open("50_states.csv") as data_file:
        csv_entries = csv.reader(data_file)
        for entry in csv_entries:
            # Filter out the column header entry, add the rest.
            if entry[0] != "state":
                data["states"][entry[0]] = {
                    # x,y coordinates on game screen to print label.
                    "x": int(entry[1]),
                    "y": int(entry[2]),
                    # Flag to exclude this state if it has been guessed.
                    "added": False,
                }


def ask_for_input(data):
    user_input = screen.textinput(title="Guess the State", prompt="What is a state name?").title()
    if user_input in data["states"]:
        # State guessed is present in db.
        if not data["states"][user_input]["added"]:
            # State guessed has already been guessed previously.
            data["states"][user_input]["added"] = True
            print("Yes")
        else:
            # Handle states that have already been correctly guessed.
            print("Already Guessed This State")
    else:
        # Handle incorrectly guessed state.
        print("No")


setup_game_window(screen)
import_state_data(db)
while True:
    ask_for_input(db)
        #check_input()
            #if input in data:
                #add_label()
                #add_point()
            #else
                #game_over()


screen.exitonclick()
