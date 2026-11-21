from turtle import Turtle

class Snake:
    def __init__(self): #Cria o corpo da cobra
        self.x_pos = 0
        self.snakes = []
        for _ in range(3):
            self.snake = Turtle('square')
            self.snake.color('white')
            self.snake.penup()
            self.snake.goto(self.x_pos, 0)
            self.x_pos -= 20
            self.snakes.append(self.snake)

        self.head = self.snakes[0]
        self.head.color('red')
        self.tail = self.snakes[-1]

    def move(self):
        for snake in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake - 1].xcor()
            new_y = self.snakes[snake - 1].ycor()
            self.snakes[snake].goto(new_x, new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() == 270:
            self.head.setheading(270)
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            self.head.setheading(90)
        else:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            self.head.setheading(0)
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            self.head.setheading(180)
        else:
            self.head.setheading(0)


    # def def_tail_heading(self):   Metodo que eu estava usando para aumentar a cobra  DESNECESSARIO
    #     if self.snakes[-2].xcor() == self.tail.xcor() + 20:
    #         self.tail.setheading(0)
    #     elif self.snakes[-2].xcor() == self.tail.xcor() - 20:
    #         self.tail.setheading(180)
    #     elif self.snakes[-2].ycor() == self.tail.ycor() + 20:
    #         self.tail.setheading(90)
    #     elif self.snakes[-2].ycor() == self.tail.ycor() - 20:
    #         self.tail.setheading(270)

    def gets_bigger(self):
        self.snake = Turtle('square')
        self.snake.color('white')
        self.snake.penup()
        self.snake.goto(self.snakes[-1].position())
        self.snakes.append(self.snake)
        # if self.tail.heading() == 0:      Metodo que eu estava usando para aumentar a cobra  DESNECESSARIO
        #     self.snake.goto(self.tail.xcor() - 20, self.tail.ycor())
        # elif self.tail.heading() == 180:
        #     self.snake.goto(self.tail.xcor() + 20, self.tail.ycor())
        # elif self.tail.heading() == 90:
        #     self.snake.goto(self.tail.xcor(), self.tail.ycor() - 20)
        # elif self.tail.heading() == 270:
        #     self.snake.goto(self.tail.xcor(), self.tail.ycor() + 20)
        # self.snakes.append(self.snake)
        # self.tail = self.snakes[-1]

    def gets_snake_body_location_pos(self):
        positions = []
        for snake in self.snakes:
            position = (round(snake.xcor()), round(snake.ycor()))
            positions.append(position)

        return positions