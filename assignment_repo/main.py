import pygame, pgzero, pgzrun, sys

# Version checks (kept)
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

from src.game import WIDTH as _W, HEIGHT as _H, TITLE as _T
WIDTH = _W
HEIGHT = _H
TITLE = _T

from src.app import App

# sounds exists in this module at runtime; pass it in so Game can play sounds without importing builtins
app = App(sounds)

def update():
    # Thin delegate
    app.update()

def draw():
    # Thin delegate (screen exists here at runtime)
    app.draw(screen)

# Start music (kept)
try:
    pygame.mixer.quit()
    pygame.mixer.init(44100, -16, 2, 1024)

    music.play("theme")
    music.set_volume(0.3)
except:
    pass

pgzrun.go()
