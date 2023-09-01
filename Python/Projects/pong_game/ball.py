from turtle import Turtle

# constants
COLOUR = "white"
SHAPE = "circle"


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOUR)
        self.shape(SHAPE)
        self.penup()

    # vertical = 1 if up -1 if down, horizontal 1 if right, -1 if left
    def move(self, vertical, horizontal):
        new_x = self.xcor() + horizontal * 10
        new_y = self.ycor() + vertical * 10
        self.goto(new_x, new_y)
