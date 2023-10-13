from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        # self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_a_car()


    def create_a_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        init_x = random.randint(100, 300)
        init_y = random.randint(-240, 240)
        self.goto(init_x, init_y)

    def car_move(self, win_times):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE - win_times * MOVE_INCREMENT * 0.2
        self.goto(new_x, self.ycor())


