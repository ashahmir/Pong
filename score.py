from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self, player):
        self.y = 0
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        if player == 1:
            self.goto(-100, 230)
        else:
            self.goto(100,230)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Michroma", 40, "normal"))
        time.sleep(1)

    def match_win(self, player):
        self.goto(0,-20)
        self.write(f"Player {player} won the match", align="center", font=("Michroma", 20, "normal"))
