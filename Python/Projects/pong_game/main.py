from turtle import Screen

# ToDo: main screen
# ToDo: score
# ToDo: paddles
# ToDo: ball (creation and moves, boucing, collision with paddle)
# ToDo: gameover logic

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOUR = "black"
SCREEN_TITLE = "Pong game"

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOUR)
screen.title(SCREEN_TITLE)



screen.exitonclick()