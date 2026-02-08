from src.game import draw_text, set_game

class PauseScreen:
    """
    Pause mode: freezes simulation by NOT calling game.update().
    Draws the current play scene + overlay.
    """
    def __init__(self, app, play_screen):
        self.app = app
        self.play_screen = play_screen
        # Ensure global 'game' pointer still refers to the active play game
        set_game(self.play_screen.game)

    def update(self, input_state):
        # Press P again to resume
        if input_state.pause_pressed:
            self.app.change_screen(self.play_screen)

    def draw(self, screen):
        # Draw the frozen scene (play screen's draw does not advance simulation)
        self.play_screen.draw(screen)

        # Overlay
        draw_text(screen, "PAUSED", 200)
        draw_text(screen, "PRESS P", 240)
