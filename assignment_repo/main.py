# main.py (or the original file reduced to Pygame Zero entrypoints delegating to App)

from random import choice, randint, random, shuffle
from enum import Enum
import pygame, pgzero, pgzrun, sys

# Version checks (kept from original)
if sys.version_info < (3, 5):
    print("This game requires at least version 3.5 of Python. Please download it from www.python.org")
    sys.exit()

pgzero_version = [int(s) if s.isnumeric() else s for s in pgzero.__version__.split('.')]
if pgzero_version < [1, 2]:
    print(
        "This game requires at least version 1.2 of Pygame Zero. You have version {0}. "
        "Please upgrade using the command 'pip3 install --upgrade pgzero'".format(pgzero.__version__)
    )
    sys.exit()

# Import constants from the refactored game module and re-export them for Pygame Zero
from src.game import WIDTH as _W, HEIGHT as _H, TITLE as _T
WIDTH = _W
HEIGHT = _H
TITLE = _T

from src.app import App

app = App()

def update():
    # Thin delegate (required)
    app.update()

def draw():
    # Thin delegate (required)
    app.draw()

# Set up sound system and start music (kept from original)
try:
    pygame.mixer.quit()
    pygame.mixer.init(44100, -16, 2, 1024)

    music.play("theme")
    music.set_volume(0.3)
except:
    pass

pgzrun.go()
