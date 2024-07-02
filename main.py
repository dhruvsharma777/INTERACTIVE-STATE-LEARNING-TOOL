import turtle
import pandas
screen = turtle.Screen()
screen.title("India States Game")
image = "make.gif"

screen.addshape(image)
turtle.shape(image)
count = []
while len(count)<34:
    answer = screen.textinput(title=f"{len(count)}/28Guess the State", prompt="What's another state's name?").title()

    data = pandas.read_csv("28_states.csv")
    all_states=data.state.to_list()
    if answer == "Exit":
        missing_states =[state for state in all_states if state not in count]

        # for state in all_states:
        #     if state not in count:
        #         missing_states.append(state)
        new_Data=pandas.DataFrame(missing_states)
        new_Data.to_csv("Missed states.csv")
        break

    if answer in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        count.append(answer)
        cor=data[data.state == answer]
        t.goto(int(cor.x.iloc[0]), int(cor.y.iloc[0]))
        t.write(answer)


turtle.exitonclick()
