from turtle import Turtle, addshape


class Invader(Turtle):
    def __init__(self):
        super().__init__()
        addshape("invader.gif")
        self.shape("invader.gif")
