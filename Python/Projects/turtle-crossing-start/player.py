from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.set_turtle_parameters()
        self.set_starting_position()
        self.score = 0

    def set_turtle_parameters(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)

    def set_starting_position(self):
        self.setposition(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def add_score(self):
        self.score += 1

    def cross_finish_line(self):
        self.add_score()
        self.set_starting_position()

    def if_finish_line_crossed(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.cross_finish_line()
        else:
            pass
