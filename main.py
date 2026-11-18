from turtle import Turtle,Screen
import time
from ball import Ball
from paddle import Paddle
from score_board import Scoreboard

# setting up the window
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My Pong game")
screen.tracer(0)

# forming the paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
#forming the ball
ball = Ball()
#forming the scoreboard
scoreboard_1 = Scoreboard((-150,180))
scoreboard_2 = Scoreboard((150,180))
#controling paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# operating the game
game_on=True
x=0.1
while game_on:
    screen.update()
    time.sleep(x)
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    if ball.xcor() > 380:
        ball.goto(0,0)
        ball.reset_position()
        scoreboard_1.increase_score()
        x-=0.0001
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.reset_position()
        scoreboard_2.increase_score()
        x-=0.0001




screen.exitonclick()