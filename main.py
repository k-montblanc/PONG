import random
import time
from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

#create screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PONG")
screen.tracer(0)
#create paddles

right_paddle = Paddle()
left_paddle = Paddle()
right_paddle.goto(350,0)
left_paddle.goto(-350,0)
#create scoreboard
left_score = Scoreboard()
left_score.goto(150,250)
left_score.create_scoreboard()
right_score = Scoreboard()
right_score.goto(-150, 250)
right_score.create_scoreboard()
#draw center lines
center_line = Turtle()
center_line.hideturtle()
center_line.penup()
center_line.goto(0, 300)
center_line.pencolor("white")
center_line.setheading(270)
center_line.pendown()
for i in range(0,10):
    for i in range(0, 3):
        center_line.forward(10)
        center_line.penup()
        center_line.forward(10)
        center_line.pendown()

#paddle movement
screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
#create ball
ball = Ball()

still_playing = True
while still_playing:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()
    # detect collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) <50 and ball.xcor() < -320:
        # ball.xmove += 10
        # ball.ymove += 10
        ball.bounce_x()
        # ball.increase_speed()
    if ball.xcor() > 380:
        left_score.add_points()
        ball.reset_ball()
    elif ball.xcor() < -380:
        right_score.add_points()
        ball.reset_ball()








# def determine_angle:
#     relative_intersect_y = (left_paddle.ycor() + (5/2))




screen.exitonclick()
