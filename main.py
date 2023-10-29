import turtle as t
import pandas
import string

# Variables
score = 0
max_score = 50
found = set()

# Set background
screen = t.getscreen()
screen.bgpic("blank_states_img.gif")

# Make turtle invisible
t.hideturtle()
t.up()

# Import data
data = pandas.read_csv("50_states.csv")


def draw_state(state):
    state_data = data[data.state == state]
    t.setposition(state_data.x.item(), state_data.y.item())
    t.write(state, font=("Arial", 10, "normal"))


while score < 50:
    user_input = string.capwords(t.textinput(f"{score}/{max_score} States Correct",
                                             "Enter a state name (type exit to end game):"))

    if user_input == "Exit":
        break

    if len(data[data.state == user_input]) > 0:
        if user_input not in found:
            found.add(user_input)
            score += 1
            draw_state(user_input)

t.mainloop()
