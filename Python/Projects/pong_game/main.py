from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# ToDo: main screen ==> Done
# ToDo: score ==> done
# ToDo: paddles ==> Done
# ToDo: ball (creation and moves, boucing, collision with paddle) ==> done
# ToDo: gameover logic
# ToDo: add max and min for movement of paddle ==> done
# ToDo: bug Blockade for bouncing ball withn paddle
# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_BACKGROUND_COLOUR = "black"
SCREEN_TITLE = "Pong game"
WALL_BOUNCE = 270
DISTANCE_FROM_PADDLE = 50
X_FOR_BOUNCE_PADDLE = 320
X_FOR_SCORE = 380
# creation of objects
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND_COLOUR)
screen.title(SCREEN_TITLE)
screen.tracer(0)

# right paddle
paddle_1 = Paddle(1)
# left paddle
paddle_2 = Paddle(2)
ball = Ball()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")


while game_is_on:
    time.sleep(ball.moves_speed)
    screen.update()
    ball.move()

    # collision with the wall
    if ball.ycor() > WALL_BOUNCE or ball.ycor() < -WALL_BOUNCE:
        ball.wall_bounce()

    # collision with paddle
    if (ball.distance(paddle_1) < DISTANCE_FROM_PADDLE and ball.xcor() > X_FOR_BOUNCE_PADDLE) or (ball.distance(paddle_2) < DISTANCE_FROM_PADDLE and ball.xcor() < -X_FOR_BOUNCE_PADDLE):
        ball.paddle_bounce()

    # score for a paddle
    if ball.xcor() > X_FOR_SCORE or ball.xcor() < -X_FOR_SCORE:
        if ball.xcor() > X_FOR_SCORE:
            scoreboard.paddle_2_point()
            print("score 2")
        else:
            scoreboard.paddle_1_point()
        ball.starting_position()


screen.exitonclick()