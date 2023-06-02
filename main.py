from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

score = 0

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

def move_left():
    snake.move_snake("left")

def move_right():
    snake.move_snake("right")

def move_up():
    snake.move_snake("up")

def move_down():
    snake.move_snake("down")

def moving_snake():
    return snake.move_snake("forward")

        
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Left", fun=move_left)
screen.onkeypress(key="Right", fun=move_right)
screen.onkeypress(key="Up", fun=move_up)
screen.onkeypress(key="Down", fun=move_down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.25)
    game_is_on = moving_snake()
    if not game_is_on:
        # If the Snake is not moving, I hit a wall and the game is over.
        print("Game Over!!!")
        print(f"Your score is: {scoreboard.score}")
        scoreboard.game_over()
    else:
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increment_score()
            snake.add_segment()
        


screen.exitonclick()