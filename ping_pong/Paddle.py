import turtle
# Paddle class
class Paddle1:
    def __init__(self, x_position,y_pos=0):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("Red")
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_position,y_pos)



    def move_up(self):
        y = self.paddle.ycor()
        if y < 250:  # Keep paddle within window
            y += 20
        self.paddle.sety(y)
    def set_s(self,x,y):
        self.paddle.shapesize(stretch_wid=x, stretch_len=y)

    def move_down(self):
        y = self.paddle.ycor()
        if y > -240:  # Keep paddle within window
            y -= 20
        self.paddle.sety(y)

    def Collision_New(self,ball):
            # Paddle and ball collision
            if (10 > ball.ball.xcor() > -10) and (
                    self.paddle.ycor() + 50 > ball.ball.ycor() > self.paddle.ycor() - 50):
                # ball.ball.sety(180)
                ball.bounce_x()

            elif (10 < ball.ball.xcor() < -10) and (
                    self.paddle.ycor() + 50 > ball.ball.ycor() > self.paddle.ycor() - 50):
                # ball.ball.sety(-180)
                ball.bounce_x()
