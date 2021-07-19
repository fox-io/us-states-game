import csv
import turtle

# Constants for readability.
GAME_OVER = "gg"


class GuessTheStates:
    """Guess the States

    A game in which the player guesses the 50 states of the United States of America."""
    def __init__(self):
        """Setup the main window and create internal variables."""
        # Setup the main window.
        self.window = turtle.Screen()
        self.window.title("Guess the States")
        self.window.setup(width=725, height=491)
        self.window.addshape("blank_states_img.gif")
        turtle.shape("blank_states_img.gif")

        # Initialize class variables.
        self.data = {}
        self.points = 0
        self.prompt_text = ""
        self.user_input = ""
        self.duplicate_guess = False

        self.labeler = turtle.Turtle()
        self.labeler.penup()
        self.labeler.hideturtle()

    def import_state_data(self):
        """Imports the list of states and their screen coordinates from a CSV file."""
        with open("50_states.csv") as data_file:
            csv_entries = csv.reader(data_file)
            for entry in csv_entries:
                # Filter out the column header entry, add the rest.
                if entry[0] != "state":
                    self.data[entry[0]] = {
                        # x,y coordinates on game screen to print label.
                        "x": int(entry[1]),
                        "y": int(entry[2]),
                        # Flag to exclude this state if it has been guessed.
                        "added": False,
                    }

    def get_input(self):
        """Prompts the user for the name of a state and checks if it is correct or not."""
        # Set default prompt
        self.prompt_text = "What is the name of a state?"
        if self.duplicate_guess:
            # If previous guess was a duplicate, inform user.
            self.prompt_text = "You've already guessed that state. Try again."

        # Get the user's guess.
        self.user_input = self.window.textinput(title=f"Guess the State [{self.points}/50]", prompt=self.prompt_text).title()

        self.duplicate_guess = False
        if self.user_input in self.data:
            # State guessed is present in db.
            if not self.data[self.user_input]["added"]:
                # State guessed has already been guessed previously.
                self.data[self.user_input]["added"] = True
                self.points += 1
                self.add_state_label()
                if self.points == 50:
                    self.labeler.goto(0, 0)
                    self.labeler.color = "green"
                    self.labeler.write(f"You Win!\n{self.points}/50 Correct", False, "center", ("Arial", 36, "bold"))
            else:
                # Handle states that have already been correctly guessed.
                self.duplicate_guess = True
        else:
            # Handle incorrectly guessed state.
            self.labeler.color("red")
            self.labeler.goto(0, -40)
            self.labeler.write(f"Game Over!\n{self.points}/50 Correct", False, "center", ("Arial", 36, "bold"))
            return GAME_OVER

    def add_state_label(self):
        """Shows text with the name of the state at the coordinates provided."""
        self.labeler.goto(self.data[self.user_input]["x"], self.data[self.user_input]["y"])
        self.labeler.write(self.user_input, False, "center", ("Arial", 8, "normal"))


game = GuessTheStates()
game.import_state_data()
while True:
    result = game.get_input()
    if result == GAME_OVER:
        break

game.window.exitonclick()
