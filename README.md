# 🏓 Python Pong Game

A classic retro Pong game built in Python using the `turtle` graphics library and Object-Oriented Programming (OOP) principles.

---

## 🚀 Features

* **Two-Player Local Multiplayer:** Play head-to-head with a friend on the same keyboard.
* **Dynamic Ball Physics:** The ball bounces off the top/bottom boundaries and deflects off paddles upon successful collision.
* **Progressive Difficulty:** The ball's speed gradually increases with each successful paddle hit (`x -= 0.0001`).
* **Real-Time Scoreboard:** Tracks and updates scores dynamically for both players whenever a point is scored[cite: 4, 6].
* **Modular OOP Architecture:** Clean separation of concerns with dedicated classes for the ball, paddles, and scoreboard[cite: 4, 5, 6, 7].

---

## 🛠️ Project Structure

```text
├── main.py          # Main game loop, window setup, and collision handling
├── ball.py          # Ball class managing movement, bounces, and resets
├── paddle.py        # Paddle class controlling position and vertical movement
└── score_board.py   # Scoreboard class handling score tracking and text rendering
