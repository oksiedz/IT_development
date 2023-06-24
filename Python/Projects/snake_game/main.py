from turtle import Screen, Turtle

# screen configuration
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake game")

snake = []

# creation of first snake created from 3 squares
for x in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.penup()
    new_turtle.color("white")
    new_turtle.goto(x * - 20, 0)
    snake.append(new_turtle)








screen.exitonclick()