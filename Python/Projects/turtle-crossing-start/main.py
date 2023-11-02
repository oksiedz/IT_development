import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
list_of_cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 1:
        list_of_cars.append(CarManager(player.game_level))

    screen.onkey(player.move_forward, "Up")

    # instruction checking if turtle crossed the finish line and then performing action
    if player.if_finish_line_crossed():
        player.cross_finish_line()
        scoreboard.print_value(player.game_level)
        for car in list_of_cars:
            car.set_movement_speed(level=player.game_level)
    else:
        pass

    for car in list_of_cars:
        car.move_car()
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
