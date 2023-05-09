from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake_is_on = True
while snake_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect collison with the food.
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.final_score()
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()

    #Detect colllison with tail
    for segment in snake.segment[1:]:
        pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()
            # scoreboard.final_score()

screen.exitonclick()
