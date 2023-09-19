
from turtle import Turtle

SCORES_LOCATION = "/Users/brent/OneDrive/Desktop/Scores.txt"
class ScoreBoard(Turtle):
    #class attributes?

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.score = 0
        with open(SCORES_LOCATION, mode="r") as file:
            self.highscore = int(file.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", False, align = "left", font = ("Arial", 10, "normal"))


    def increase(self, amount):
        self.clear()
        self.score += amount
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        if self.score > self.highscore:
            print("saving score...")
            with open(SCORES_LOCATION, mode="w") as file:
                # Converting ints to string with an F string!
                file.write(f"{self.score}")
        self.write("GAME OVER", align = "center", font = ("Arial", 35, "bold"))
