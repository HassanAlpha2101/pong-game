from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position)
        self.write(self.score,align="center",font=("time",80,"normal"))
        self.hideturtle()
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(self.score,align="center",font=("time",80,"normal"))
