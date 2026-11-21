from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x= 0, y= 280)
        self.score = 0
        self.scoreboard = f"Score: {self.score}"
        self.write_score()

    def write_score(self):
        self.write(self.scoreboard, False, "center", ('Arial', 14, 'normal'))


    def add_score(self):
        self.clear()
        self.score += 1
        self.scoreboard = f"Score: {self.score}"
        self.write_score()


    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', False, "center", ('Arial', 24, 'normal'))




