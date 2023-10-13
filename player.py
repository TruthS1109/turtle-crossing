from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()


    def create_player(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def restart(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER. ", align="center", font=("Courier", 24, "normal"))

