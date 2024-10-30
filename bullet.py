from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, ship):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.hideturtle()
        self.shapesize(stretch_wid=1, stretch_len=0.25)
        self.bulletspeed = 25
        self.ship = ship
        self.state = "ready"

    def shoot(self):
        x = self.ship.xcor()
        y = self.ship.ycor() + 10
        self.goto(x, y)
        self.state = "fire"
        self.showturtle()
