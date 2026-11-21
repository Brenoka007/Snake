from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('red')
        self.create_wall()


    def create_wall(self):
        self.goto(-270,-270)
        self.pendown()
        self.goto(270, -270)
        self.goto(270, 270)
        self.goto(-270, 270)
        self.goto(-270, -270)
        self.penup()