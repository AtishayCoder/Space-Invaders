from turtle import Screen
from space_ship import HomeShip
from bullet import Bullet
from invader import Invader
from invader_positions import INVADER_POSITIONS
import time
import random

all_aliens = []

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Space invaders")
screen.bgcolor("black")
screen.tracer(0)

home_ship = HomeShip()
bullet = Bullet(home_ship)

for pos in INVADER_POSITIONS:
    new_invader = Invader()
    new_invader.goto(pos)
    all_aliens.append(new_invader)

screen.listen()
screen.onkeypress(home_ship.go_right, "Right")
screen.onkeypress(home_ship.go_left, "Left")
screen.onkeypress(bullet.shoot, "space")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if bullet.state == "fire":
        y = bullet.ycor()
        y += bullet.bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 290:
        bullet.hideturtle()
        bullet.state = "ready"

    for enemy in all_aliens:
        if bullet.distance(enemy) < 30:
            bullet.goto(10000000, 90909090900)
            enemy.goto(209090909090, 77779078787878)

    if random.randint(0, 6) == 4:
        for enemy in all_aliens:
            enemy.goto(enemy.xcor(), enemy.ycor() - 10)

    for enemy in all_aliens:
        if enemy.distance(home_ship) < 20 or enemy.ycor() == -150:
            print("You lose!!!")
            quit()

    if len(all_aliens) < 1:
        print("You win!!!")
        quit()

screen.exitonclick()
