import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pointer = turtle.Turtle()
pointer.penup()
pointer.hideturtle()

data = pandas.read_csv("50_states.csv")
correct_name = 0
all_states = data.state.to_list()
guessed_states = []
not_guessed = []

while correct_name < 50:
    answer_state = screen.textinput(
        title=f"Correct guessed: {correct_name}/{len(data.state)}", prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        break

    for state_name in data["state"]:
        if answer_state == state_name:
            state = data[data.state == state_name]
            guessed_states.append(state_name)
            pointer.goto(int(state.x),int(state.y))
            pointer.write(f"{state_name}")
            correct_name += 1

for state in all_states:
    if state not in guessed_states:
        not_guessed.append(state)

pandas.DataFrame(not_guessed).to_csv("missed.csv")
