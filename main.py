from turtle import Turtle, Screen
import time
from Player import Player
from score import Scoreboard
from ball import Ball

liner = Turtle()


def draw_line(on):
    if on:
        y = 270
        liner.penup()
        liner.hideturtle()
        liner.color("white")
        for a in range(15):
            liner.goto(0, y)
            liner.write("I", align="center", font=("Roboto", 20, "bold"))
            y -= 40
    else:
        liner.clear()


# Screen Setup
screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
screen.title(titlestring="Pong")
screen.tracer(0)
game_on = False
target = int(screen.textinput(prompt="Enter the Target Score: ", title="Score Setup"))
if target:
    game_on = True

player1 = Player(1)
player2 = Player(2)
score1 = Scoreboard(1)
score2 = Scoreboard(2)
ball = Ball()


# Drawing the line
draw_line(game_on)

screen.listen()
screen.onkeypress(player2.up, "Up")
screen.onkeypress(player2.down, "Down")
screen.onkeypress(player1.up, "w")
screen.onkeypress(player1.down, "s")


while game_on:
    time.sleep(0.04)
    screen.update()
    for x in range(4):
        if player1.player[x].distance(ball) < 30:
            ball.bounce_from_player()
    for x in range(4):
        if player2.player[x].distance(ball) < 30:
            ball.bounce_from_player()

    if ball.xcor() > 350:
        ball.bounce_from_walls()
        score1.score += 1
        score1.update_score()

    if ball.xcor() < -350:
        ball.bounce_from_walls()
        score2.score += 1
        score2.update_score()

    if ball.ycor() < -290:
        ball.bounce_from_ground()

    if ball.ycor() > 290:
        ball.bounce_from_ground()

    if ball.xcor() > 0:
        ball.color("blue")
    else:
        ball.color("red")

    if score1.score == target:
        score1.match_win("blue")
        game_on = False

    if score2.score == target:
        score2.match_win("red")
        game_on = False

    ball.move_ball()

draw_line(game_on)
screen.exitonclick()

# Credits: a.shahmir
