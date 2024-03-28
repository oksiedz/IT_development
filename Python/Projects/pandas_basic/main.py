import turtle
import pandas

IMAGE = "US_game/blank_states_img.gif"
STATE_DATA = "US_game/50_states.csv"
screen = turtle.Screen()
screen.title("U.S.A. States guessing game")
screen.addshape(IMAGE)

turtle.shape(IMAGE)

# method reading the coordinates from the click on map
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

answered_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").lower()
data = pandas.read_csv(filepath_or_buffer=STATE_DATA)
row_with_answer = data[data.state.str.lower() == answered_state]
# new turtle which will be writting answers
writer_turtle = turtle.Turtle()
writer_turtle.penup()
writer_turtle.hideturtle()
writer_turtle.goto(int(row_with_answer.x), int(row_with_answer.y))
writer_turtle.write(row_with_answer.state.str)
print(row_with_answer.state.str)
print(row_with_answer)
print(answered_state)

turtle.mainloop()
# screen.exitonclick()
