from turtle import Turtle
from random import choice

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('green')
        self.speed('fastest')
        self.positions = [-260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
        self.refresh([(0,0), (-20, 0), (-40, 0)])

    def refresh(self, invalid_pos):
        random_x = choice(self.positions)
        random_y = choice(self.positions)
        while (random_x, random_y) in invalid_pos:
            random_x = choice(self.positions)
            random_y = choice(self.positions)

        self.goto(x=random_x, y= random_y)







