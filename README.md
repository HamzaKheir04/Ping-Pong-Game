🏓 Ping-Pong Game

A simple two-player Ping Pong game built with Python and the turtle graphics module.

🎮 How to Play

PlayerMove UpMove DownPlayer A (left paddle)WSPlayer B (right paddle)↑ Arrow↓ Arrow


The first player to score the most points before time runs out wins.
Two extra moving obstacle paddles are placed in the middle of the field for added challenge.
The game lasts 30 seconds by default (configurable in main.py).


📂 Project Structure

ping_pong/
├── main.py        # Game loop, screen setup, scoring, and timer
├── Ball.py         # Ball class: movement and bouncing logic
├── Paddle.py        # Paddle class: player and obstacle paddle behavior
└── Functions.py       # Helper functions: collisions, borders, game over screen

▶️ Requirements


Python 3.x
turtle module (comes pre-installed with standard Python)


🚀 Run the Game

bashpython main.py

🛠️ Features


Two-player controls (keyboard)
Score tracking and live display
Countdown timer with game-over screen
Randomly colored obstacle paddles in the middle of the field
Ball collision detection with paddles and screen borders

