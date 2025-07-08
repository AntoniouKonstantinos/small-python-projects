import turtle
import pandas
from statesnames import StatesNames

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_answers = []
pen = StatesNames()

data = pandas.read_csv("50_states.csv")
names = data["state"].to_list()

while len(correct_answers) < 50:
    answer_state = screen.textinput(f"{len(correct_answers)}/50 States Correct", "What's another state's name ?").title()
    if answer_state == "Exit":
        missing_states = []
        for name in names:
            if name not in correct_answers:
                missing_states.append(name)
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break
    if answer_state in names:
        correct_answers.append(answer_state)
        state_data = data[data["state"] == answer_state]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        pen.write_name(x_cor, y_cor, answer_state)


