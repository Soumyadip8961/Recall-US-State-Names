import turtle
import pandas

tim=turtle.Turtle()
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


user_answer = screen.textinput(title="Guess tha State", prompt="Guess another state's name: ")
answer=user_answer.title()
#print(user_answer)


data=pandas.read_csv("50_states.csv")
#print(data)
name_data=data["state"].to_list()
#print(name_data[6])


count=0
game_is_on=True
guessed_state=[]
while game_is_on:
    if answer in name_data:
        tim.penup()
        tim.hideturtle()
        x_cor=data[data.state==answer].x
        y_cor=data[data.state==answer].y
        tim.goto(int(x_cor), int(y_cor))
        tim.write(answer, move=False)

        if answer in guessed_state:

            user_answer = screen.textinput(title=f"{answer} is already in the map", prompt="Guess another state's name: ")
            answer = user_answer.title()
            # print(answer)

        elif answer not in guessed_state:
            count += 1
            guessed_state.append(answer)
            user_answer=screen.textinput(title=f"{count}/50 States Correct", prompt="Guess another state's name: ")
            answer=user_answer.title()

    else:
        user_answer = screen.textinput(title=f"{answer} is wrong", prompt="Guess another state's name: ")
        answer = user_answer.title()



    if count >= 50:
        game_is_on=False

    if answer == "Exit":
        break


for state in guessed_state:
    if state in name_data:
        name_data.remove(state)
print("Remaining States:",name_data)
remain_states=pandas.DataFrame(name_data)
remain_states.to_csv("States to learn.csv")



