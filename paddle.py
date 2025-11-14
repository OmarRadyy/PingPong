from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
    def go_up(self):
        if self.ycor() < 230:
            self.sety(self.ycor()+40)
    def go_down(self):
        if self.ycor() > -230:
            self.sety(self.ycor()-40)