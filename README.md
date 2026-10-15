<div align="center">

# Select-the-Star - Try to Select the Randomly set Star

![Python](https://img.shields.io/badge/Python-3-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

*A command-line, interface-based game where you need to input the location of the star built with [Python](https://www.python.org/).*

## Gameplay Example

![Gameplay Screenshot 1](./images/image_01.png)

</div>

## Features

1. The `os`, `sys`, and `random` modules are used to give the player an improved experience by clearing all previous actions from the screen and allowing a smooth exit midway through the game.

## The Stack

| Category | Details |
| --- | --- |
| Language | Python 3 |
| Standard Library | `os`, `sys`, `random` |
| Interface | Terminal / command-line (Unix-like) |
| Tooling | Git, any Python-capable IDE (e.g. VSCodium) |
| License | MIT |

## Project Structure

```text
├── select-the-star.py # Game
├── images/
│   └── image_01.png   # Gameplay example
└── LICENSE
```

## Prerequisites

1. This application can only be run if you have Python installed or run it through the IDE of your choice.

2. Everything is intended to be run on a Unix or Unix-like system but more concrete Windows support is coming.  Everything will work if you are on MacOS, Linux, the BSD of your choice, or running through Windows Subsystem for Linux.

### Applications and Software

- **Python** - Download from [python.org](https://www.python.org/) or via your OS package manager.
- **Integrated Development Environment** - A good example would be [VSCodium](https://vscodium.com/), but anything will do as long as it can run Python programs.

## Installation

Clone this repository using the **Clone** button above, or download the source archive, then place the files in a directory of your choice.

### For use of the terminal

```bash
mkdir ~/Code/select-the-star

# Clone or extract this repository into ~/Code/select-the-star/
```

**Notes:**

The repository can be downloaded manually and be placed in any directory of your choice as long as all of the files remain together.

## Start and Play the Game

### Start the Game

```bash
cd ~/Code/select-the-star

python3 select-the-star.py
```

### Play the Game

1. Enter a number to choose the location of a row or column.

2. Entering anything other than an integer, 'exit', or 'y' to begin the game will fail.

## What I Improved

- **Standard library fluency:** used `os` and `sys` to clear the terminal and handle clean mid-game exits without external dependencies.
- **Documentation and version control:** wrote user-facing install/play instructions and tracked the project with Git.
- **Random generation:** used `random` to randomly generate a number for the row and column the number will be located in each time the user guesses both.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Benjamin (Ben) LaShell
