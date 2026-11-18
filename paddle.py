from turtle import Turtle,Screen
import time

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        screen = Screen()
# the paddle generation
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        time.sleep(0.1)

    def go_up(self):
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

# controlling the paddle


