# 🏓 Python Pong Game

A classic retro Pong game built in Python using the `turtle` graphics library and Object-Oriented Programming (OOP) principles.

## 🚀 Features
* **Two-Player Support:** Play locally with a friend (Left paddle: `W` / `S`, Right paddle: `Up` / `Down` arrow keys).
* **Dynamic Ball Physics:** The ball bounces off top/bottom walls and increases speed as it successfully hits paddles.
* **Scoreboard System:** Real-time score tracking for both players with clean on-screen rendering.
* **OOP Architecture:** Clean, modular codebase separated into specialized classes for the Ball, Paddles, and Scoreboard.

---

## 🛠️ Project Structure

```text
├── main.py          # Main game loop, window setup, and collision handling
├── paddle.py        # Paddle class controlling movement and positioning
├── ball.py          # Ball class handling movement, speed, and bounces
└── score_board.py   # Scoreboard class managing scores and text rendering
