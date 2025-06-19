from turtle import Turtle

ALIGNMENT = "center"
FONT = ("courier", 18, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("crimson")
        self.write("GAME OVER", False, ALIGNMENT, FONT)