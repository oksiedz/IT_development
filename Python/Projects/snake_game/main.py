from turtle import Screen
from snake import Snake
from food import Food
import time

# screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)  # parameter responsible for screen not updating automatically

snake = Snake()
food = Food()
# enabling listening of the keyboard
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)  # one second daly after each snake's segment moves
    snake.move()
    # detection of collision of snake and food (used by distance)
    if snake.snake_head.distance(food) < 15:
        # 15 since size of food is 10x10 circle
        # food should go to random location
        food.new_food_location()

screen.exitonclick()
