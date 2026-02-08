from pgzero.builtins import screen
from src.game import Game, set_game

class MenuScreen:
    def __init__(self, app):
        self.app = app
        # Background game (no player) like original menu
        self.game = Game()
        set_game(self.game)

    def update(self, input_state):
        if input_state.start_pressed:
            from src.screens.play import PlayScreen
            self.app.change_screen(PlayScreen(self.app))
            return

        # Keep background animating like original
        self.game.update(None)

    def draw(self):
        self.game.draw()

        # Title overlay like original
        screen.blit("title", (0, 0))

        # "Press SPACE" animation like original
        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))
