from turtle import Turtle

FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", False, "left", FONT)

    "Updates the level of the game and displays it"
    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", False, "left", FONT)

    """Display the 'GAME OVER' when we lose"""
    def game_over(self):
        self.goto(0,0)
        self.color("crimson")
        self.write("GAME OVER", False, "center", ("Courier", 27, "bold"))