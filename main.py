import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
cars = []
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.tracer(0)

#initialize with 10 cars
for _ in range(10):
    cars.append(CarManager())

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
game_loop_num = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    game_loop_num += 1
    # Create a new card evert 6 loop
    if game_loop_num == 6:
        cars.append(CarManager())
        game_loop_num = 0

    for car in cars:
        car.car_move(scoreboard.score)
        ###Drop the cars reaching the left side of screen
        if car.xcor() < -320:
            cars.remove(car)

        # detect Collision between the turtle and cars
        if player.distance(car) < 20:
            player.game_over()
            game_is_on = False

    #check if the turtle reaches the top side and win the game
    if player.ycor() > 280:
        scoreboard.add_point()
        player.restart()

screen.exitonclick()




