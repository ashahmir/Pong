from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.direction = 15
        self.angle = 150
        self.shape("circle")
        self.color("white")
        self.setheading(self.angle)

    def move_ball(self):
        self.penup()
        self.forward(self.direction)

    def bounce_from_player(self):
        self.direction *= -1
        self.right(45)

    def bounce_from_walls(self):
        self.goto(0,0)

    def bounce_from_ground(self):
        self.right(-135)

    def bounce_from_top(self):
        self.right(135)
