from pgzero.builtins import screen
from src.game import draw_status, set_game

class GameOverScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game
        set_game(self.game)

    def update(self, input_state):
        if input_state.start_pressed:
            from src.screens.menu import MenuScreen
            self.app.change_screen(MenuScreen(self.app))
            return

    def draw(self):
        self.game.draw()
        draw_status()
        screen.blit("over", (0, 0))
