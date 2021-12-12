from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup of the Screen___________________________________________________________________________________________________

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# object of the paddle
r_paddle = Paddle((350, 0))
r_paddle.color("blue")
l_paddle = Paddle((-350, 0))
l_paddle.color("green")

# object of the ball
ball = Ball()

# object of the scoreboard
scoreboard = Scoreboard()

# ______________________________________________________________________________________________________________________


# up n down-------------------------------------------------------------------------------------------------------------


screen.listen()
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball. incrz_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball need bounce
        ball.bounce_y()

    # Detect collision with wall
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # # Detect l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
# ______________________________________________________________________________________________________________________

screen.exitonclick()
