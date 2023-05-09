
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Segoe UI Semibold", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/Arit/Desktop/data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 20
        # self.clear()
        self.update_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     # self.clear()
    #     self.write("Game Over!", align=ALIGNMENT, font=FONT)
    #
    # def final_score(self):
    #     self.goto(x=0, y=40)
    #     self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as d:
                d.write(f"{self.high_score}")
        self.score = 0
        self.update_score()


