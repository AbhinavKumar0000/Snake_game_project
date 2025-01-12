  
from turtle import Screen

from scoreboard import Scoreboard
from snka import Snake
import time
from food import Food

screen = Screen()
food = Food()
scoreboard = Scoreboard()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
score = 0
screen.tracer(0)


snake = Snake()
screen.listen()
screen.onkey(key="Up",fun= snake.up)
screen.onkey(key="Down",fun= snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun= snake.left)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    #food detection
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase()


    #wall detection
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()


    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()












screen.exitonclick()