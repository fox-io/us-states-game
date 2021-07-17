import turtle

screen = turtle.Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

answer_state = screen.textinput(title="Guess the State", prompt="What is a state name?")

screen.exitonclick()
