import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.move_distance = None
        self.set_starting_attributes()
        self.set_starting_position()
        self.setheading(180)
        self.set_movement_speed(level)

    def set_starting_attributes(self):
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2, outline=None)
        self.fillcolor(random.choice(COLORS))

    def set_starting_position(self):
        starting_x_cor = random.randrange(-260, 260)
        self.sety(starting_x_cor)
        self.setx(280)

    def move_car(self):
        self.forward(self.move_distance)

    def set_movement_speed(self, level):
        self.move_distance = STARTING_MOVE_DISTANCE + (level - 1) * MOVE_INCREMENT
