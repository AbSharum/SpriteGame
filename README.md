# Sprite Game

A small Pygame prototype: a character sprite chases/flees the mouse cursor on a full-screen window with a slowly cycling background color, plus a couple of sound-effect "cheat" keys. Not a full game — more of a playground for sprite movement and animation.

`Game/name.py` (the entry point) does the following:

- Initializes Pygame and opens a window at the current display resolution.
- Loads `Images/ABJump.gif`, `Images/shid.jpeg`, `Images/GojoPic.jpg`, and `Images/Sukuna.jpg`, scales them to 200x200, and loads `Sounds/CandyShop.mp3`, `Sounds/Gojo.wav`, `Sounds/Bruh.mp3`, and `Sounds/Money Go.wav`.
- Continuously cycles the background fill color and moves the main sprite toward/away from the mouse position each frame, flipping the sprite horizontally depending on direction of travel.
- Keyboard controls: `W`/`A`/`S`/`D` move the first sprite; arrow keys move a second (currently invisible/unused) sprite rect; `G` flashes a Gojo image + plays `Gojo.wav`; `B` flashes a Sukuna image + plays `Money Go.wav`.
- Plays a "Bruh" sound effect once the sprite's rect center matches the mouse position and hides the mouse cursor while overlapping.
- Closes on window-quit event.

## Contents

- `Game/` — `name.py` script plus the `Images/` and `Sounds/` assets it loads.
- `Sprites/` — Piskel sprite source file (`.piskel`) and an exported animation gif, used to author the character art in `Game/Images/`.

## Stack

Python 3 with [Pygame](https://www.pygame.org/).

## Setup & Running

```
pip install pygame
```

Run from inside the `Game/` directory (the script loads assets via relative paths like `Sounds/...` and `Images/...`):

```
cd Game
python name.py
```

Note: this is an early prototype — mostly assets with a single driving script, not a full game yet. There are also some rough edges (e.g. the arrow-key-controlled second sprite/image can cause a crash on first use of `G`/`B` if pressed out of order, since a couple of variables are only initialized once the mouse loop runs at least one iteration).
