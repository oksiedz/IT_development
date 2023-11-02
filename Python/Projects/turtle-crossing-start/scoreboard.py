from turtle import Turtle

FONT = ("Courier", 24, "normal")
STARTING_LEVEL = 1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(-270, 260)
        self.print_value(STARTING_LEVEL)

    def print_value(self, score):
        self.clear()
        print_string = f'LeveL: {score}'
        self.write(arg=print_string,  font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER",align="center", font=FONT)