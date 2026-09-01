# 🐍 Python Snake

A simple terminal-based Snake game written in Python.

This project is a small exercise in learning Python fundamentals such as **2D lists, coordinates, loops, random numbers, and basic game state management**.

## 🎮 Features

* 12 × 4 terminal game area
* Snake represented by `=`
* Apple represented by `*`
* Random apple placement
* Snake automatically moves across the scene
* Snake grows when it eats an apple
* Terminal screen refreshes every frame
* Simple game loop

## 🛠️ Requirements

* Python 3.x
* Windows terminal

No external Python packages are required.

## ▶️ Running the Game

Clone or download the project, then run:

```bash
python snake.py
```

The game will continuously refresh the terminal as the snake moves.

## 📁 Project Structure

```text
.
├── snake.py
└── README.md
```

## 🧠 What This Project Demonstrates

The project uses several basic Python concepts:

### 2D Lists

The game world is represented as a list of rows:

```python
scene = [
    [' ' for _ in range(WIDTH)]
    for _ in range(HEIGHT)
]
```

### Coordinates

The snake and apple use `(x, y)` coordinates to keep track of their positions.

### Random Numbers

The apple is placed randomly using Python's `random` module.

### Game Loop

The game continuously updates the scene inside a `while True` loop.

### Terminal Refresh

The screen is cleared before each frame:

```python
os.system("cls")
```

### Timing

A short delay controls the game speed:

```python
time.sleep(0.2)
```

## 🚧 Current Limitations

This is an early/simple version of Snake.

* No keyboard controls
* Snake moves automatically
* No score system
* No collision detection with the snake's body
* No game-over screen
* Small play area

## 🔮 Possible Improvements

Future versions could add:

* `W/A/S/D` or arrow-key controls
* Score tracking
* Game-over conditions
* Wall collision
* Self-collision
* Increasing difficulty
* Larger game area
* Start and pause screens
* Better terminal rendering
* Cross-platform screen clearing

## 📚 Purpose

This project is primarily a **Python learning exercise** rather than a polished game.

The goal is to understand how a simple game can be represented as data and updated repeatedly inside a program.

## 📄 License

This project is free to use, modify, and experiment with.
