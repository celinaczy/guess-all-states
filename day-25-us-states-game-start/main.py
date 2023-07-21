import turtle
import pandas as pd

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("states game")
screen.setup(width=700)

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

df = pd.read_csv("50_states.csv")

score = 0
correct_guesses = []
states_list = df["state"].to_list()

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.color("black")

while len(correct_guesses) < 50:
    answer = screen.textinput(title=f"{score}/50 states correct", prompt="Name a state")
    answer = answer.title()
    if answer == "Exit":
        break

    if answer in states_list and answer not in correct_guesses:
        score += 1
        correct_guesses.append(answer)
        cor_x = int(df[df.state == answer].x.item())
        cor_y = int(df[df.state == answer].y.item())
        writer.goto(cor_x,cor_y)
        writer.write(answer, align=ALIGNMENT, font=FONT)


for i in range(len(correct_guesses)):
    states_list.remove(correct_guesses[i])
print(states_list)

data_frame = pd.DataFrame(states_list)
print(data_frame)
data_frame.to_csv("missing_states.csv")
screen.exitonclick()
