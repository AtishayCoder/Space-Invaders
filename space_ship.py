from turtle import Turtle, addshape

Y_POS = -150


class HomeShip(Turtle):
    def __init__(self):
        super().__init__()
        addshape("player.gif")
        self.shape("player.gif")
        self.penup()
        self.goto(0, Y_POS)

    def go_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, Y_POS)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, Y_POS)
