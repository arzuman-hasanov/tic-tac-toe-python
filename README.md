# Tic-Tac-Toe — Python Terminal Game

A simple **two-player Tic-Tac-Toe game** built with Python and designed to run directly in the terminal.

The game uses a 3×3 board and allows players to enter moves using coordinates such as `A1`, `B2`, or `C3`.

## Overview

This project was created as a Python programming exercise to practice fundamental programming concepts, including:

* Variables and data structures
* Functions
* Loops
* Conditional statements
* User input
* Input validation
* NumPy arrays
* Game-state management
* Win and draw detection

## How the Game Works

The game is played by two players:

* Player 1: `X`
* Player 2: `O`

Players take turns selecting an empty square on the board.

The board uses the following coordinate system:

```text
  -------------
A |   |   |   |
  -------------
B |   |   |   |
  -------------
C |   |   |   |
  -------------

    1   2   3
```

For example:

```text
A1
B2
C3
```

are valid moves.

## Game Rules

The game follows the standard Tic-Tac-Toe rules.

A player wins when they place three of their symbols in:

* A horizontal row
* A vertical column
* A diagonal

If all nine squares are occupied without a winner, the game ends in a draw.

## Technologies Used

* Python
* NumPy

## Main Components

### Board

The game board is represented using a NumPy 3×3 array:

```python
board = np.array([
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
])
```

The values represent the state of each square:

```text
0 → Empty
1 → X
2 → O
```

### Move Coordinates

A dictionary converts human-readable coordinates into board positions:

```python
moves = {
    "A1": (0, 0),
    "A2": (0, 1),
    "A3": (0, 2),
    "B1": (1, 0),
    "B2": (1, 1),
    "B3": (1, 2),
    "C1": (2, 0),
    "C2": (2, 1),
    "C3": (2, 2)
}
```

This allows players to enter moves such as `A1` instead of entering array indices.

### Win Detection

The `check_victory()` function checks:

* Rows
* Columns
* Main diagonal
* Opposite diagonal

and determines whether a player has achieved three matching symbols.

### Input Validation

The program checks whether:

1. The entered move is a valid coordinate.
2. The selected square is not already occupied.

If the move is invalid, the player is asked to enter another move.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/tic-tac-toe-python.git
cd tic-tac-toe-python
```

### 2. Install NumPy

```bash
pip install numpy
```

### 3. Run the game

```bash
python tic_tac_toe.py
```

## Example

A game might look like:

```text
********************
Turn 1 : Player X
********************

  -------------
A |   |   |   |
  -------------
B |   |   |   |
  -------------
C |   |   |   |
  -------------

    1   2   3

Enter your move: A1
```

Players continue entering coordinates until one player wins or the game ends in a draw.

## Project Structure

```text
tic-tac-toe-python/
│
├── tic_tac_toe.py
├── README.md
└── requirements.txt
```

## What I Learned

This project helped me practice the fundamentals of Python programming, particularly:

* Working with arrays
* Creating and using functions
* Managing program state
* Writing game logic
* Handling user input
* Validating user actions
* Using loops to control program flow
* Checking multiple conditions

## Possible Improvements

Some possible future improvements would be:

* Add a graphical interface
* Add a single-player mode against a computer
* Implement an AI opponent using the Minimax algorithm
* Keep track of player scores
* Add a restart option
* Make the game platform-independent instead of relying on terminal-specific commands
* Improve the user interface
