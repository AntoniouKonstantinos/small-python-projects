from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.draw_net_and_score()

    #Draws the middle net and moves turtle to the top so it can write the score
    def draw_net_and_score(self):
        self.penup()
        self.goto(0, -280)
        self.pendown()
        self.setheading(90)
        self.color("white")
        self.pensize(5)
        for _ in range(10):
            self.forward(30)
            self.penup()
            self.forward(30)
            self.pendown()
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"{self.l_score}    {self.r_score}", False, "center", ("Courier", 36, "bold"))

    #Updates player scores according to the flag value
    def update_score(self, flag):
        if flag == 1:
            self.l_score += 1
        else:
            self.r_score += 1
        self.clear()
        self.draw_net_and_score()