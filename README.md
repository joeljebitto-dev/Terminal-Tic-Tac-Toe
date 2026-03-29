# Terminal Tic-Tac-Toe

A simple two-player Tic-Tac-Toe game that runs in the terminal, built with Python.

## Features

- Two-player local gameplay
- Terminal-based board rendering
- Win and draw detection
- Start a new game without restarting the script
- Quit at any time from the command line
- No external dependencies

## Requirements

- Python 3.10 or newer

## Getting Started

### Clone the repository

```bash
git clone https://github.com/joeljebitto-dev/Terminal-Tic-Tac-Toe.git
cd Terminal-Tic-Tac-Toe
```

### Run the game

```bash
python game.py
```

If needed, use:

```bash
python3 game.py
```

## How to Play

The game is played by two players in the terminal.

When prompted, enter your move as coordinates in tuple format:

```text
(x, y)
```

Example:

```text
(1, 3)
```

## Controls

- `q` — quit the game
- `n` — start a new game

## Rules

- Player 1 and Player 2 take turns placing their marks on the board.
- The first player to align three marks in a row, column, or diagonal wins.
- If all cells are filled and nobody wins, the game ends in a draw.

## Project Structure

```text
Terminal-Tic-Tac-Toe/
└── game.py
```

## Code Overview

The project is implemented in a single Python file and includes logic for:

- Board initialization
- Board rendering
- Move validation and placement
- Turn switching
- Win checking
- Draw checking
- Restart and quit handling

## Customization

The default player names are set in the script:

```python
xo.local_setup("player 1", "player 2")
```

You can change them directly in `game.py`, for example:

```python
xo.local_setup("Joel", "Alex")
```

## Future Improvements

- Safer input handling without `eval`
- Single-player mode against an AI
- Score tracking across rounds
- Improved board UI
- Unit tests for game logic
- Packaging as an installable CLI app

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
