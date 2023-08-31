from turtle import Screen
from paddle import Paddle

# ToDo: main screen ==> Done
# ToDo: score
# ToDo: paddles ==> Done
# ToDo: ball (creation and moves, boucing, collision with paddle)
# ToDo: gameover logic

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOUR = "black"
SCREEN_TITLE = "Pong game"

# creation of objects
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOUR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

paddle_1 = Paddle(1)
paddle_2 = Paddle(2)

game_is_on = True

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


while game_is_on:
    screen.update()




screen.exitonclick()