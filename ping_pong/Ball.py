import turtle
import random
class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(1)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        # self.x =random.randint(-390,390)
        # self.y = random.randint(-290,290)
        self.ball.goto(0, 0)
        self.ball.dx = 0.1 # Ball movement speed in x direction
        self.ball.dy = 0.1  # Ball movement speed in y direction

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def Setter_Shape(self, NShape):
        self.ball.shape(NShape)


    def bounce_y(self):
        self.ball.dy *= -1

    def bounce_x(self):
        self.ball.dx *= -1

    def reset_position(self):
        self.ball.goto(0, 0)
        self.bounce_x()


