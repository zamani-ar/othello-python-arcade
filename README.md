# ♟️ Othello (Reversi) Game — Python Arcade Implementation

A fully playable implementation of the classic Othello (Reversi) board game built using Python and the `Arcade` game development library.

The project implements:

* Complete Othello game logic
* Disc flipping mechanics
* Move validation
* Turn management
* Interactive graphical interface

---

# Features

## ✅ Fully Playable Othello Game

* Two-player local gameplay
* Interactive mouse-based controls
* Real-time board updates
* Automatic disc flipping
* Turn tracking system

---

# Game Mechanics

The implementation includes the core Othello/Reversi rules:

* Horizontal flipping
* Vertical flipping
* Diagonal flipping
* Legal move detection
* Board state management

The game dynamically computes all available moves for each player and updates the board accordingly after every move.

---

# GUI Implementation

The graphical interface is built using the `Arcade` Python library.

## Interface Features

* 8×8 interactive game board
* Black and white disc rendering
* Move highlighting
* Turn indicator
* Mouse click interaction

---

# Technical Highlights

## Core Components

### Board Management

The game board is represented using a 2D matrix structure for efficient state updates.

### Move Validation

Implemented directional search algorithms to validate legal moves across:

* Horizontal directions
* Vertical directions
* Diagonal directions

### Disc Flipping Engine

Automatically flips opponent discs according to official Othello rules after each valid move.

### Event-driven GUI

Uses Arcade’s event system for:

* Rendering
* Mouse interaction
* Game updates

---

# Technologies Used

* Python
* Arcade

---

# Project Structure

```text id="t1r8wp"
main.py
├── Board rendering
├── Move validation
├── Disc flipping logic
├── Turn management
└── GUI interaction
```

---

# Running the Project

## Install Dependencies

```bash id="h5jlwm"
pip install arcade
```

## Run the Game

```bash id="dyc1rj"
python main.py
```

---

# Gameplay Preview

```text id="5svw4y"
Black Player Turn
↓
Select valid position
↓
Flip opponent discs
↓
Switch turn
↓
Repeat until board is filled
```

---

# Learning Objectives

This project explores:

* Game development with Python
* Event-driven programming
* GUI programming
* Board-game logic implementation
* State management
* Algorithmic move validation

---

# Future Improvements

Potential future enhancements include:

* AI opponent (Minimax / Alpha-Beta pruning)
* Score tracking
* End-game detection
* Restart functionality
* Sound effects and animations
* Multiplayer networking
* Better UI design

---

# Disclaimer

This project was developed as an educational/course project for learning game development and algorithmic board-game implementation in Python.
