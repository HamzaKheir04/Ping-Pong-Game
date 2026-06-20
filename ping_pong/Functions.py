import random

def display_Timer(timer_pen, time_left):
    timer_pen.clear()
    timer_pen.write(f"Time Left: {time_left} sec", align="center", font=("Courier", 24, "normal"))

def GameOver(timer_pen, Score_A, Score_B):
    timer_pen.clear()
    timer_pen.goto(0, 0)
    if Score_A > Score_B:
        message = f"Game Over!\nFinal Score:\nPlayer A: {Score_A}  Player B: {Score_B}\nResult: Player A Won :)"
    elif Score_B > Score_A:
        message = f"Game Over!\nFinal Score:\nPlayer A: {Score_A}  Player B: {Score_B}\nResult: Player B Won :)"
    else:
        message = f"Game Over!\nFinal Score:\nPlayer A: {Score_A}  Player B: {Score_B}\nResult: Draw!"
    timer_pen.write(message, align="center", font=("Courier", 24, "normal"))

def random_color():
    r = random.random()  # Generate a random float between 0 and 1
    g = random.random()
    b = random.random()
    return (r, g, b)


def Border_check(ball, Score_A, Score_B):
    if ball.ball.ycor() > 290:
        ball.ball.sety(290)
        ball.bounce_y()

    if ball.ball.ycor() < -290:
        ball.ball.sety(-290)
        ball.bounce_y()

    if ball.ball.xcor() > 390:
        ball.reset_position()
        Score_A += 1

    if ball.ball.xcor() < -390:
        ball.reset_position()
        Score_B += 1
    return Score_A, Score_B    


def Collision(ball, paddle_a, paddle_b):
    # Paddle and ball collision
    if (350 > ball.ball.xcor() > 340) and (
            paddle_b.paddle.ycor() + 50 > ball.ball.ycor() > paddle_b.paddle.ycor() - 50) and ball.ball.dx > 0:
       # ball.ball.setx(340)
        ball.bounce_x()

    if (-350 < ball.ball.xcor() < -340) and (
            paddle_a.paddle.ycor() + 50 > ball.ball.ycor() > paddle_a.paddle.ycor() - 50)and ball.ball.dx < 0:
        #ball.ball.setx(-340)
        ball.bounce_x()

