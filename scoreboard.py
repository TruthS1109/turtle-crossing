from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.write("SCORE: " + str(self.score), align="center", font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()



