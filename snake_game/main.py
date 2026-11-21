import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from wall import Wall

#Creates the screen for the game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
wall = Wall()


screen.listen()

screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left,'a')
screen.onkey(snake.right,'d')
game_on = True

while game_on:
    screen.update()
    time.sleep(0.15)
    #TODO: deixar o usuario mudar a dificuldade no time.sleep
    #TODO: game starts only when the user press a key

    snake.move()

    if snake.head.distance(food) < 15:
        score.add_score()
        #asnake.def_tail_heading()   Metodo que eu estava usando para aumentar a cobra  DESNECESSARIO
        snake.gets_bigger()
        position = snake.gets_snake_body_location_pos()
        food.refresh(position)

    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        score.game_over()
        game_on = False

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False





screen.exitonclick()










