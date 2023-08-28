from turtle import Turtle

MOVE_DISTANCE=20

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        # creation of first snake created from 3 squares
        for x in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color("white")
            # starting positions of the snake are set here
            new_turtle.goto(x * - 20, 0)
            self.snakes.append(new_turtle)

    # snake movement, changing coordination from the last segment to the new previous one
    def move (self):
        for snake_piece in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_piece - 1].xcor()
            new_y = self.snakes[snake_piece - 1].ycor()
            self.snakes[snake_piece].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)


Snake

