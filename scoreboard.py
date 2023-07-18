from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.write(f"Score : {self.score}  High Score: {self.highscore}", True, align="center", font=("Arial", 10, "normal"))
        self.hideturtle()
        
    def score_display(self):
        self.score += 1
        self.clear()
        self.goto(0,280)
        self.write(f"Score : {self.score} High Score: {self.highscore}", True, align="center", font=("Arial", 10, "normal"))
        
    def display_game_over(self):
        if self.highscore < self.score :
            self.highscore = self.score
        self.clear()
        self.goto(0,280)
        self.score = 0
        self.write(f"Score : {self.score} High Score: {self.highscore}", True, align="center", font=("Arial", 10, "normal"))
        
        