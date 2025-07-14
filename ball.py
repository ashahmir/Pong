from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.angle = 150
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10

    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_from_player(self):
        self.move_x *= -1

    def bounce_from_walls(self):
        self.goto(0,0)

    def bounce_from_ground(self):
        self.move_y *= -1

