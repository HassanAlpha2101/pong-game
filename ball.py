from turtle import Screen,Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_direction = 10
        self.x_direction = 10

    def move(self):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_direction *=-1
    def x_bounce(self):
        self.x_direction *= -1
    def reset_position(self):
        self.goto(0,0)
        self.x_bounce()







