import random
import turtle
import time
from Paddle import Paddle1  # Import classes from the separate file
from Functions import GameOver, display_Timer, random_color, Border_check, Collision
from Ball import Ball


# Set up the screen
win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Initialize paddles, ball, score, and timer
paddle_a = Paddle1(-350)
paddle_b = Paddle1(350)
paddle_b.paddle.color("blue")
ball = Ball()



bad = Paddle1(0, -180)
bad2 = Paddle1(0, 180)
bad.paddle.color(random_color())
bad2.paddle.color(random_color())

Score_A = 0
Score_B = 0

# Modification That Dr.Ahmad Asked :
bad.set_s(3, 1)
bad2.set_s(3, 1)

# Display initial score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write(f"Player A: {Score_A} | Player B: {Score_B}",
                align="center", font=("Courier", 24, "normal"))


# Timer setup
timer_pen = turtle.Turtle()  # turtle is created to display the remaining time on the screen.
timer_pen.speed(0)
timer_pen.color("white")
timer_pen.penup()
timer_pen.hideturtle()
timer_pen.goto(0, 220)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a.move_up, "w")
win.onkeypress(paddle_a.move_down, "s")
win.onkeypress(paddle_b.move_up, "Up")
win.onkeypress(paddle_b.move_down, "Down")

# Main game loop
start_time = time.time()
game_duration = 30 # 60 seconds

while True:
    win.update()
    # Calculate time left
    # The elapsed_time is calculated using time.time()
    # to track how much time has passed since the game started.
    elapsed_time = time.time() - start_time
    time_left = int(game_duration - elapsed_time)
    display_Timer(timer_pen, time_left)
    # The time_left is calculated by subtracting the elapsed_time from game_duration.
    # If time_left reaches 0, the game loop breaks, and the game ends.
    # Check if time is up
    if time_left <= 0:
        break  # End the game loop when time runs out

    # Move the ball
    ball.move()

    # Border_Check
    Score_A, Score_B = Border_check(ball, Score_A, Score_B)
    score_pen.clear()
    score_pen.write(f"Player A: {Score_A} | Player B: {Score_B}",
                align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    Collision(ball, paddle_a, paddle_b)

    # Modification That Dr.Ahmad Asked :
    bad.Collision_New(ball)
    bad2.Collision_New(ball)

GameOver(timer_pen, Score_A, Score_B)
# Keep the window open until the user closes it\
win.mainloop()