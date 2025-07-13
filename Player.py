from turtle import Turtle


class Player:
    def __init__(self, player):
        self.x_cord = 0
        self.y_cord = -40
        self.player = []
        for x in range(4):
            _player = Turtle("square")
            if player == 1:
                _player.color("blue")
                self.x_cord = -335
            else:
                _player.color("red")
                self.x_cord = 330
            _player.penup()
            _player.goto(self.x_cord, self.y_cord)
            _player.right(90)
            self.player.append(_player)
            self.y_cord += 20

    def up(self):
        if self.player[len(self.player) - 1].ycor() < 280:
            for x in range(len(self.player) - 1, -1, -1):
                y_pos = self.player[x].ycor() + 20
                self.player[x].goto(self.player[x].xcor(), y_pos)

    def down(self):
        if self.player[0].ycor() > -280:
            for x in range(len(self.player) - 1, -1, -1):
                y_pos = self.player[x].ycor() - 20
                self.player[x].goto(self.player[x].xcor(), y_pos)
