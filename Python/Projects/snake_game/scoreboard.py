from turtle import Turtle

INITIAL_VALUE = 0
INITIAL_X = 0
INITIAL_Y = 260
ALIGNMENT = "center"
FONT_STYLE = ("Arial", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.value = INITIAL_VALUE
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(INITIAL_X, INITIAL_Y)
        self.print_score()

    def increase_score(self):
        self.value = self.value + 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write("Score: " + str(self.value), align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.clear()
        self.write("Game Over Your Score: " + str(self.value), align=ALIGNMENT, font=FONT_STYLE)
