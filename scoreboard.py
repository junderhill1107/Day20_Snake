from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0,280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))


    def increment_score(self):
        self.score += 1
        self.refresh_scoreboard()


    def refresh_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "normal"))

    
    def game_over(self):
        super().__init__()
        self.goto(0,0)
        self.color("white")
        self.hideturtle()
        self.write(f"Game Over", align="center", font=("Arial", 10, "normal"))