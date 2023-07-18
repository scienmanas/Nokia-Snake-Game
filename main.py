from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect Collosion with food
    
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_display()
        snake.create_new_segment()
    
    # Detecting the collosion with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.display_game_over()
        snake.reset()
        food.refresh()
        
    # Detecting the Collosion with wall
    if snake.is_collision() == True :
        score.display_game_over()
        snake.reset()
        food.refresh()
        
        
        

screen.exitonclick()