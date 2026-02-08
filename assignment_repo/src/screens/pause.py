# pause.py (optional separate screen)

from src.game import draw_text, set_game

class PauseScreen:
    def __init__(self, app, play_screen):
        self.app = app
        self.play_screen = play_screen
        set_game(self.play_screen.game)

    def update(self, input_state):
        # Press P again to resume
        if input_state.pause_pressed:
            self.app.change_screen(self.play_screen)

    def draw(self):
        # Draw the frozen scene
        self.play_screen.draw()
        # Overlay
        draw_text("PAUSED", 200)
        draw_text("PRESS P", 240)
